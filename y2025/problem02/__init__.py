from typing import *


def part1(inp: str):
    sum = 0
    for id_range in inp.split(","):
        start, end = map(int, id_range.split("-"))

        # you can find the invalid IDs by looking for any ID which is made only
        # of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64
        # twice), and 123123 (123 twice) would all be invalid IDs.

        for id in range(start, end + 1):
            id_str = str(id)
            if len(id_str) % 2 != 0:
                continue
            half_point = len(id_str) // 2
            invalid = id_str[0:half_point] == id_str[half_point:]
            if invalid:
                sum += id
    return sum


def part2(inp: str):
    return 0
