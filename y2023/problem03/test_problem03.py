from y2023.problem03 import *

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_part1_example():
    assert part1(example) == 4361

    ex2 = """..*.
.123
...."""

    assert part1(ex2) == 123


def test_part2_example():
    assert part2(example) == 467835
