from . import *

example_map = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


def test_parse_map():
    m = Map.parse_map(example_map)
    assert m.rows == 11
    assert m.at(0, 0) == "."
    assert m.at(1, 0) == "."
    assert m.at(2, 0) == "#"
    assert m.at(3, 0) == "#"

    # wraparound
    assert m.at(11, 0) == "."

    # bottom right most
    assert m.at(10, 10) == "#"

    assert m.at(11, 10) == "."
    assert m.at(12, 10) == "#"


def test_example_part1():
    direction = (3, 1)
    assert count_trees(example_map, direction) == 7
