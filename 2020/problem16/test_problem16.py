from problem16 import *

inp1 = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""


def test_part1_example():
    assert part1(inp1) == 71


inp2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""


def test_part2_determine_rule_order():
    rules, mine, nearby = parse_input(inp2)
    assert determine_rule_order(rules, [mine, *nearby]) == {
        0: "row",
        1: "class",
        2: "seat",
    }
