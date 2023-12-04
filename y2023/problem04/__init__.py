from typing import *


def part1(inp: str):
    total = 0
    for line in inp.split("\n"):
        # print(line)
        numbers = line.split(": ")[1]
        winning, have = numbers.split("| ")
        winners = {int(s) for s in winning.split()}
        mine = {int(s) for s in have.split()}
        num_winners = len(winners & mine)
        if num_winners > 0:
            total += 1 << (num_winners - 1)
    return total


def part2(inp: str):
    pass
