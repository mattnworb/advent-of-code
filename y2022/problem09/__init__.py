from typing import *
from enum import Enum

Position = Tuple[int, int]
Directions = List[Tuple[str, int]]


def parse(inp: str) -> Directions:
    ds = []
    for line in inp.strip().split("\n"):
        sp = line.split(" ")
        assert len(sp[0]) == 1
        ds.append((sp[0], int(sp[1])))
    return ds


def simulate(directions: Directions, knotcount: int) -> int:
    knots = [(0, 0) for n in range(knotcount)]

    visited: Set[Position] = set()
    visited.add((0, 0))

    for move in directions:
        d, count = move
        for _ in range(count):
            # first determine new position for head knot
            hx, hy = knots[0]
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

            knots[0] = hx, hy

            # then move each subsequent knot
            for n in range(1, len(knots)):
                hx, hy = knots[n - 1]
                tx, ty = knots[n]

                # figure out how to move this knot
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

                knots[n] = tx, ty

            # remember where tail has been
            visited.add(knots[-1])

    return len(visited)


def part1(inp: str):
    directions = parse(inp)
    return simulate(directions, 2)


def part2(inp: str):
    directions = parse(inp)
    return simulate(directions, 10)
