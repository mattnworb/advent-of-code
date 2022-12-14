from typing import *
import json

Packet = Union[list["Packet"], int]


def parse(inp: str) -> List[Tuple]:
    packets: List[Tuple] = []
    for section in inp.split("\n\n"):
        left, right = map(json.loads, section.split("\n"))
        packets.append((left, right))
    return packets


def compare(left: Packet, right: Packet) -> Optional[bool]:
    # both lists
    if type(left) == list and type(right) == list:
        for ix in range(max(len(left), len(right))):
            # check if left has run out
            if ix >= len(left):
                return True
            if ix >= len(right):
                return False
            # compare items
            c = compare(left[ix], right[ix])
            if c == True or c == False:
                return c
        # continue onto next item
        return None

    # both ints
    if type(left) == int and type(right) == int:
        if left == right:
            return None
        return left < right

    # one must be an int
    if type(left) == list:
        right = [right]
        return compare(left, [right])
    else:
        return compare([left], right)


def part1(inp: str):
    pairs = parse(inp)
    n = 0
    for ix, pair in enumerate(pairs):
        left, right = pair
        if compare(left, right) == True:
            n += ix + 1
    return n


def part2(inp: str):
    pass
