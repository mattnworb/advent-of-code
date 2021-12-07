from y2021.problem07 import *

example = """16,1,2,0,4,2,7,1,2,14"""


def test_part1_example():
    # TODO: populate
    assert part1(example) == 37


def test_least_distance():
    assert least_distance(parse_input(example), pt1cost) == (2, 37)


def test_pt2cost():
    assert pt2cost(16, 5) == 66
    assert pt2cost(5, 16) == 66
    assert pt2cost(1, 5) == 10


def test_part2_example():
    # TODO: populate
    assert part2(example) == 168
