from typing import *


def parse_input(inp: str) -> List[Tuple[Set[int], Set[int]]]:
    pairs = []
    for line in inp.split("\n"):
        left, right = line.split(",")
        l1, l2 = left.split("-")
        r1, r2 = right.split("-")
        pairs.append(
            (
                set(range(int(l1), int(l2) + 1)),
                set(range(int(r1), int(r2) + 1)),
            )
        )
    return pairs


def part1(inp: str):
    return sum(p1.issubset(p2) or p2.issubset(p1) for p1, p2 in parse_input(inp))


def part2(inp: str):
    return sum(len(p1 & p2) > 0 for p1, p2 in parse_input(inp))
