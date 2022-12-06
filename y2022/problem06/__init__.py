from typing import *

# The device will send your subroutine a datastream buffer (your puzzle input);
# your subroutine needs to identify the first position where the four most
# recently received characters were all different. Specifically, it needs to
# report the number of characters from the beginning of the buffer to the end of
# the first such four-character marker.


def find_marker(inp: str, size: int) -> int:
    for i in range(len(inp) - (size - 1)):
        if len(set(inp[i : i + size])) == size:
            return i + size
    return -1


def part1(inp: str):
    # start-of-packet marker = first 4 chars in stream that are non-repeating
    return find_marker(inp, 4)


# Your device's communication system is correctly detecting packets, but still
# isn't working. It looks like it also needs to look for messages.
#
# A start-of-message marker is just like a start-of-packet marker, except it
# consists of 14 distinct characters rather than 4.
def part2(inp: str):
    return find_marker(inp, 14)
