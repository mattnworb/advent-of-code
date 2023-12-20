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


# def test_move_rocks():
#     assert move_rocks_left(["O...O#O"]) == ["OO...#O"]
#     assert move_rocks_left(["#.#OO#..O", "..O#..#.O"]) == ["#.#OO#O..", "O..#..#O."]


# def test_transpose():
#     # 12
#     # 34
#     assert transpose(["12", "34"]) == ["13", "24"]

#     m = ["12", "34", "56"]
#     assert transpose(m) == ["135", "246"]
#     assert transpose(transpose(m)) == m


# def test_rotate_cw():
#     assert rotate_cw(["12", "34"]) == ["31", "42"]
#     assert rotate_cw(rotate_cw(rotate_cw(rotate_cw(["12", "34"])))) == ["12", "34"]


def test_tilt_north():
    g = [list(line) for line in example.split("\n")]
    tilt_north(g)

    expected = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""
    assert g == [list(line) for line in expected.split("\n")]


def test_part1_example():
    assert part1(example) == 136


def test_one_spin_cycle():
    g = [list(line) for line in example.split("\n")]
    one_spin_cycle(g)

    expected = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#...."""
    assert g == [list(line) for line in expected.split("\n")]


def test_part2_example():
    assert part2(example) == 64
