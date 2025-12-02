from y2025.problem01 import *

example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_part1_example():
    assert part1(example) == 3


def test_part2_example():
    assert part2(example) == 6
