from typing import *
from collections import defaultdict

# You start by compiling a list of foods (your puzzle input), one food per line.
# Each line includes that food's ingredients list followed by some or all of the
# allergens the food contains.
#
# Each allergen is found in exactly one ingredient. Each ingredient contains
# zero or one allergen. Allergens aren't always marked; when they're listed (as
# in (contains nuts, shellfish) after an ingredients list), the ingredient that
# contains each listed allergen will be somewhere in the corresponding
# ingredients list. However, even if an allergen isn't listed, the ingredient
# that contains that allergen could still be present: maybe they forgot to label
# it, or maybe it was labeled in a language you don't know.
#
# For example, consider the following list of foods:
#
# - mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# - trh fvjkl sbzzf mxmxvkd (contains dairy)
# - sqjhc fvjkl (contains soy)
# - sqjhc mxmxvkd sbzzf (contains fish)
#
# The first food in the list has four ingredients (written in a language you
# don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might
# contain other allergens, a few allergens the food definitely contains are
# listed afterward: dairy and fish.
#
# The first step is to determine which ingredients can't possibly contain any of
# the allergens in any food in your list. In the above example, none of the
# ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the
# number of times any of these ingredients appear in any ingredients list
# produces 5: they all appear once each except sbzzf, which appears twice.

# -------------------------------------------------------------------------
# How did they figure that out?
#
# There are four foods and seven unique ingredients.
#
# The first two foods both contain dairy, so any common ingredents must be the
# one that contains dairy. Since there is only one common ingredient - mxmxvkd -
# that contains dairy.
#
# Same thing for first and last food - both contain fish. Only one ingredient is
# common: sqjhc, so that is the one that contains fish.
#
# There is only one other allergen: soy. Either sqjhc or fvjkl must contain it,
# but we already know that sqjhc contains fish, so fvjkl must contain soy.
#
# At this point we know which three ingredients contain the three known
# allergens, leaving four ingredients with no allergens.

Ingredient = str
Allergen = str
Ingredients = Set[Ingredient]


example_inp = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip()


def parse_input(inp: str) -> List[Tuple[Ingredients, Set[Allergen]]]:
    items = []

    for line in inp.strip().split("\n"):
        food, rest = line.split(" (")

        ingredients = set(food.split(" "))
        allergens = set(rest.replace("contains ", "").replace(")", "").split(", "))

        items.append((ingredients, allergens))

    return items


def solve(inp: str) -> Tuple[int, str]:
    items = parse_input(inp)

    all_allergens = set()  # all the allergens seen in the input
    recipes = []  # list of sets of ingredients, each element is one recipe

    # which ingredients could contain an allergen
    candidates: Dict[Allergen, Set[Ingredient]] = {}

    for ix, (recipe, allergens) in enumerate(items):
        all_allergens.update(allergens)

        recipes.append(recipe)

        for allergen in allergens:
            # if this is the first time we've seen an allergen, then it could be
            # any one of the ingredients in this recipe
            if allergen not in candidates:
                candidates[allergen] = set(recipe)
            else:
                # but if this is not the first recipe with this allergen, then
                # it can only be from any ingredients common to this recipe and
                # previously seen recipes
                candidates[allergen].intersection_update(recipe)

    print(f"{len(all_allergens)} unique allergens: {all_allergens}")

    for allergen in all_allergens:
        print(f"{allergen} candidate ingredients: {candidates[allergen]}")

    # Figure out which ingredients correspond to which allergens by doing the
    # following:
    # - above we keep track of which ingredients are possible for each allergen
    # - for any allergens that only have one candidate ingredient, then it must
    #   be that one - add it to the solved list
    # - remove that ingredient from the candidate list for all other allergens
    # - repeat until we have solved all the allergens

    solved: Dict[str, str] = {}

    while len(solved) != len(all_allergens):
        print(f"\nsolutions: {solved}")

        for allergen in all_allergens:
            if allergen not in solved and len(candidates[allergen]) == 1:
                solved[allergen] = next(iter(candidates[allergen]))
                print(f"allergen {allergen} must be {solved[allergen]}")
                # remove it from all other candidates
                for other_allergen, possible_ingredients in candidates.items():
                    if other_allergen == allergen:
                        continue
                    if solved[allergen] in possible_ingredients:
                        possible_ingredients.remove(solved[allergen])

    print(f"solved all allergens: {solved}")

    non_allergen_ingredients = set.union(*recipes) - set(solved.values())

    # part1: how often does each of the non-allergen ingedients occur in all the recipes?

    # part2: Arrange the ingredients alphabetically by their allergen and
    # separate them by commas to produce your canonical dangerous ingredient
    # list. (There should not be any spaces in your canonical dangerous
    # ingredient list.)
    part1 = sum(len(non_allergen_ingredients & recipe) for recipe in recipes)

    part2 = ",".join(solved[k] for k in sorted(solved.keys()))

    return part1, part2
