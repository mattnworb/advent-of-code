from y2023.problem09 import *

example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_part1_example():
    assert part1(example) == 114

    # is this right?
    ex = "1 2 5 13 33 89 245 643 1565 3535 7495 15128 29479 56181 105913 199391 377649 723582 1407901 2788593 5627669"
    assert part1(ex) == 11562151

    ex = "0 -9 -18 -27"
    assert part1(ex) == -36


def test_part2_example():
    assert part2(example) == 2
