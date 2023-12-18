from y2023.problem14 import *

example = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def test_move_rocks():
    assert move_rocks_left(["O...O#O"]) == ["OO...#O"]
    assert move_rocks_left(["#.#OO#..O", "..O#..#.O"]) == ["#.#OO#O..", "O..#..#O."]


def test_transpose():
    # 12
    # 34
    assert transpose(["12", "34"]) == ["13", "24"]

    m = ["12", "34", "56"]
    assert transpose(m) == ["135", "246"]
    assert transpose(transpose(m)) == m


def test_part1_example():
    assert part1(example) == 136


def test_part2_example():
    # TODO: populate
    # assert part2(example)
    pass
