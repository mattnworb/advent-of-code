from typing import *


# In case the Elves get hungry and need extra snacks, they need to know which
# Elf to ask: they'd like to know how many Calories are being carried by the Elf
# carrying the most Calories. In the example above, this is 24000 (carried by
# the fourth Elf).
#
# Find the Elf carrying the most Calories. How many total Calories is that Elf
# carrying?
def part1(inp: str):
    calories: List[List[int]] = []
    this_elf: List[int] = []
    for line in inp.split("\n"):
        if line == "":
            calories.append(this_elf)
            this_elf = []
        else:
            this_elf.append(int(line))
    # ignore a regression in mypy: https://github.com/python/mypy/issues/9765
    return max(map(sum, calories))  # type: ignore[arg-type,type-var]


# return sum of max 3
def part2(inp: str):
    calories: List[List[int]] = []
    this_elf: List[int] = []
    for line in inp.split("\n"):
        if line == "":
            calories.append(this_elf)
            this_elf = []
        else:
            this_elf.append(int(line))

    sums = map(sum, [1, 2, 3])  # type: ignore[arg-type]
    return sum(sorted(list(sums))[-3:])
