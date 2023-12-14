from y2023.problem13 import *

example = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def test_part1_example():
    assert part1(example) == 405


def test_change_each_char_once():
    answer = list(change_each_char_once(["#.", ".#"]))
    assert len(answer) == 4
    assert ["..", ".#"] in answer
    assert ["##", ".#"] in answer
    assert ["#.", ".."] in answer
    assert ["#.", "##"] in answer

    answer = list(change_each_char_once(["#.", ".#", ".."]))
    assert len(answer) == 6
    assert ["..", ".#", ".."] in answer
    assert ["##", ".#", ".."] in answer
    assert ["#.", "..", ".."] in answer
    assert ["#.", "##", ".."] in answer
    assert ["#.", ".#", "#."] in answer
    assert ["#.", ".#", ".#"] in answer

    answer = list(change_each_char_once(["#.#", ".##", "..."]))
    assert len(answer) == 9
    assert ["..#", ".##", "..."] in answer
    assert ["###", ".##", "..."] in answer
    assert ["#..", ".##", "..."] in answer
    assert ["#.#", "###", "..."] in answer
    assert ["#.#", "..#", "..."] in answer
    assert ["#.#", ".#.", "..."] in answer
    assert ["#.#", ".##", "#.."] in answer
    assert ["#.#", ".##", ".#."] in answer
    assert ["#.#", ".##", "..#"] in answer


def test_part2_example():
    assert part2(example) == 400

    ex2 = """.#.##.#.###
..####..##.
#########..
.##..##..##
.##..##..##
#########..
..####..##.
.#.##.#.###
#.#..#.##.#
..#####.###
...##.....#
..#..#..#..
...##...#..""".strip()
    assert part2(ex2) != 0

    ex3 = """.#..#......
..#.#......
..#...#....
#.##...####
.#..#..####
#.#.##.####
###..#.#..#""".strip()
    assert part2(ex3) != 0

    ex4 = """#.#.###
..##.##
...####
##....#
##....#
...####
..##.##
#.#.###
#.#####
....##.
.#...#.
#.#####
#....##
#..##.#
#..##.#
#..#.##
#.#####"""

    assert part2(ex4) == 1400
