from problem07 import *

example = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


def test_part1_example():
    rules = example.strip().split("\n")
    g = parse_rules(rules)
    # assert len(g) == 9

    # assert g["dotted black"] == set()
    # assert g["dark orange"] == {(3, "bright white"), (4, "muted yellow")}

    # count = 0
    # for bagname, conns in g.items():
    #     for count, name in conns:
    #         if name == "shiny gold":
    #             count += 1
    # assert count == 4
    assert expand("shiny gold", g) == {
        "bright white",
        "muted yellow",
        "dark orange",
        "light red",
    }
