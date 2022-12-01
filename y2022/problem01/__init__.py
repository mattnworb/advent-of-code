from typing import *

# In case the Elves get hungry and need extra snacks, they need to know which
# Elf to ask: they'd like to know how many Calories are being carried by the Elf
# carrying the most Calories. In the example above, this is 24000 (carried by
# the fourth Elf).
#
# Find the Elf carrying the most Calories. How many total Calories is that Elf
# carrying?
def part1(inp: str):
    calories = []
    this_elf = []
    for line in inp.split("\n"):
        if line == "":
            calories.append(this_elf)
            this_elf = []
        else:
            this_elf.append(int(line))
    return max(map(sum, calories))


def part2(inp: str):
    pass
