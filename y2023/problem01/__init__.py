from typing import *


# The newly-improved calibration document consists of lines of text; each line
# originally contained a specific calibration value that the Elves now need to
# recover. On each line, the calibration value can be found by combining the
# first digit and the last digit (in that order) to form a single two-digit
# number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
#
# In this example, the calibration values of these four lines are 12, 38, 15,
# and 77. Adding these together produces 142.
def part1(inp: str):
    total = 0
    for line in inp.split("\n"):
        digits = [int(ch) for ch in line if ch in "0123456789"]
        total += digits[0] * 10 + digits[-1]
    return total


def part2(inp: str):
    total = 0
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # this will doublecount some digits like "eightwothree" (assuming it should
    # only find [8,3]), but the problem is ambiguous about this case
    for line in inp.split("\n"):
        digits = []
        for ix, ch in enumerate(line):
            if ch in "0123456789":
                digits.append(int(ch))

            for wix, word in enumerate(words):
                if line[ix : (ix + len(word))] == word:
                    digits.append(wix + 1)

        total += digits[0] * 10 + digits[-1]
    return total
