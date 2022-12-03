from typing import *
import string


def part1(inp: str):
    lines = inp.split("\n")
    scores = []
    for line in lines:
        dupe = find_dupe(line)
        assert dupe in string.ascii_letters
        score = string.ascii_letters.find(dupe) + 1
        scores.append(score)
    return sum(scores)


def find_dupe(rucksack: str) -> str:
    l = len(rucksack)
    assert l % 2 == 0
    half = l // 2
    left, right = rucksack[:half], rucksack[half:]
    dupe = set(left) & set(right)
    assert len(dupe) == 1
    return next(iter(dupe))


def part2(inp: str):
    pass
