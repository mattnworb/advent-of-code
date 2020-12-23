from typing import *

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
Food = Set[Ingredient]


def part1(inp: str) -> int:
    pass


def parse_input(inp: str) -> List[Tuple[Food, Set[Allergen]]]:
    items = []

    for line in inp.strip().split("\n"):
        food, rest = line.split(" (")

        ingredients = set(food.split(" "))
        allergens = set(rest.replace("contains ", "").replace(")", "").split(", "))

        items.append((ingredients, allergens))

    return items
