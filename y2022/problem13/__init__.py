from typing import *
import json
import functools

Packet = Union[list["Packet"], int]


def parse1(inp: str) -> List[Tuple]:
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
    pairs = parse1(inp)
    n = 0
    for ix, pair in enumerate(pairs):
        left, right = pair
        if compare(left, right) == True:
            n += ix + 1
    return n


def parse2(inp: str) -> List[Packet]:
    packets = []
    for line in inp.split("\n"):
        if line == "":
            continue
        p = json.loads(line)
        packets.append(p)
    packets.append([[2]])
    packets.append([[6]])
    return packets


def part2(inp: str):
    packets = parse2(inp)

    def cmp(a, b) -> int:
        x = compare(a, b)
        if x == True:
            return -1
        elif x == False:
            return 1
        else:
            return 0

    sp = sorted(packets, key=functools.cmp_to_key(cmp))
    m = sp.index([[2]]) + 1
    n = sp.index([[6]]) + 1
    return m * n
