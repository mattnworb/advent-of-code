from typing import *

# The device will send your subroutine a datastream buffer (your puzzle input);
# your subroutine needs to identify the first position where the four most
# recently received characters were all different. Specifically, it needs to
# report the number of characters from the beginning of the buffer to the end of
# the first such four-character marker.


def part1(inp: str):
    size = 4
    for i in range(len(inp) - (size - 1)):
        if len(set(inp[i : i + size])) == size:
            return i + size
    return -1


def part2(inp: str):
    pass
