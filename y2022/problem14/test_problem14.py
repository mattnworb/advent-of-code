from y2022.problem14 import *

example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def test_line_between():
    assert set(line_between((498, 4), (498, 6))) == {(498, 4), (498, 5), (498, 6)}
    assert set(line_between((496, 6), (498, 6))) == {(496, 6), (497, 6), (498, 6)}
    # inverse of last call
    assert set(line_between((498, 6), (496, 6))) == {(496, 6), (497, 6), (498, 6)}


def test_part1_example():
    assert part1(example) == 24


def test_part2_example():
    # TODO: populate
    assert part2(example)
