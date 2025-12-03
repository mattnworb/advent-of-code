from typing import *


def part1(inp: str):
    # In 818181911112111, the largest joltage you can produce is 92.
    total = 0
    for bank in inp.splitlines():
        max_joltage = 0
        # need to try more than one max_digit
        for max_digit_candidate in sorted(set(bank)):
            # what if it appears more than once?
            index_of_max = bank.index(str(max_digit_candidate))

            for ix in range(index_of_max + 1, len(bank)):
                joltage = int(bank[index_of_max] + bank[ix])
                if joltage > max_joltage:
                    max_joltage = joltage

        total += max_joltage
    return total


def part2(inp: str):
    return 0
