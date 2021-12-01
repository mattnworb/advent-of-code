from . import *

ex1 = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""


# def test_parse_rules():
#     rules, _ = parse_input(ex1)
#     assert 0 in rules

#     p = rules[0]
#     assert p == "a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b"


def test_part1_example():
    assert part1(ex1) == 2
