from typing import *


def hash_alg(s: str) -> int:
    n = 0
    for ch in s:
        n += ord(ch)
        n *= 17
        n = n % 256

    assert 0 <= n <= 255
    return n


def part1(inp: str):
    strs = inp.split(",")
    return sum(map(hash_alg, strs))


def part2(inp: str):
    pass
