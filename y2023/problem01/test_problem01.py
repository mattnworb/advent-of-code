from y2023.problem01 import *


def test_part1_example():
    example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    assert part1(example) == 142


def test_part2_example():
    example = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert part2(example) == 281
