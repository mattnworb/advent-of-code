from problem11 import *

example = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip()


def test_part1_example():
    assert solve_part1(example) == 37


def test_count_visible_occupied1():
    m = """
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
"""

    assert count_visible_occupied(m.strip().split("\n"), 4, 3, debug=True) == 8


def test_count_visible_occupied2():
    m = """
.............
.L.L.#.#.#.#.
.............
"""

    assert count_visible_occupied(m.strip().split("\n"), 1, 1) == 0


def test_count_visible_occupied3():
    m = """
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
"""

    assert count_visible_occupied(m.strip().split("\n"), 3, 3) == 0


def test_count_visible_occupied4():
    m = """
#.##.##.##
#######.##
"""

    assert count_visible_occupied(m.strip().split("\n"), 0, 2, debug=True) == 5


def test_count_visible_occupied5():
    m = """
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
"""
    assert count_visible_occupied(m.strip().split("\n"), 1, 9, debug=True) == 5


def test_count_visible_occupied6():
    m = """
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
"""
    assert count_visible_occupied(m.strip().split("\n"), 2, 7, debug=True) == 0


def test_solve_part2():
    assert solve_part2(example) == 26
