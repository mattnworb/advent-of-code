from typing import *
from enum import Enum

Position = Tuple[int, int]


def parse(inp: str) -> List[Tuple[str, int]]:
    ds = []
    for line in inp.strip().split("\n"):
        sp = line.split(" ")
        assert len(sp[0]) == 1
        ds.append((sp[0], int(sp[1])))
    return ds


def part1(inp: str):
    # How many positions does the tail of the rope visit at least once?
    directions = parse(inp)

    head = tail = (0, 0)

    visited: Set[Position] = set()
    visited.add(tail)

    for move in directions:
        d, count = move
        for n in range(count):
            hx, hy = head
            tx, ty = tail

            if d == "R":
                hx += 1
            elif d == "L":
                hx -= 1
            elif d == "U":
                hy -= 1
            elif d == "D":
                hy += 1
            else:
                raise ValueError("no direction " + d)

            head = hx, hy

            # figure out how to move tail
            if hx == tx:  # same x
                if hy == ty - 2:
                    # move tail up
                    ty -= 1
                elif hy == ty + 2:
                    # move down
                    ty += 1
            elif hy == ty:  # same y
                if hx == tx - 2:
                    # move left
                    tx -= 1
                elif hx == tx + 2:
                    # move right
                    tx += 1

            # "Otherwise, if the head and tail aren't touching and aren't in the
            # same row or column, the tail always moves one step diagonally to
            # keep up"
            # if head and tail are touching diagonally, that means the
            # difference in x positions is 1 and the difference in y positions
            # is 1
            elif abs(hx - tx) > 1 or abs(hy - ty) > 1:
                # move diagonally rather than checking each of the 4 diagonals -
                # if head is above and to the right, above and to the left, etc
                # - can just check and adjust x and y separately
                if hx > tx:
                    tx += 1
                elif hx < tx:
                    tx -= 1

                if hy > ty:
                    ty += 1
                elif hy < ty:
                    ty -= 1

            tail = tx, ty

            # remember where tail has been
            visited.add(tail)

    return len(visited)


def part2(inp: str):
    pass
