from typing import *

# The pocket dimension contains an infinite 3-dimensional grid. At every integer
# 3-dimensional coordinate (x,y,z), there exists a single cube which is either
# active or inactive.
#
# In the initial state of the pocket dimension, almost all cubes start inactive.
# The only exception to this is a small flat region of cubes (your puzzle
# input); the cubes in this region start in the specified active (#) or inactive
# (.) state.
#
# The energy source then proceeds to boot up by executing six cycles.
#
# Each cube only ever considers its neighbors: any of the 26 other cubes where
# any of their coordinates differ by at most 1. For example, given the cube at
# x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at
# x=0,y=2,z=3, and so on.
#
# During a cycle, all cubes simultaneously change their state according to the following rules:
#
# - If a cube is active and exactly 2 or 3 of its neighbors are also active, the
#   cube remains active. Otherwise, the cube becomes inactive.
# - If a cube is inactive but exactly 3 of its neighbors are active, the cube
#   becomes active. Otherwise, the cube remains inactive.

# so... its a three-dimensional Conway's Game of Life
from collections import defaultdict

Position3 = Tuple[int, int, int]
State3 = Set[Position3]


def neighbors(p: Position3) -> Iterator[Position3]:
    r = range(-1, 2)
    for x in r:
        for y in r:
            for z in r:
                if not (x == y == z == 0):
                    yield p[0] + x, p[1] + y, p[2] + z


# Starting with your given initial configuration, simulate six cycles. How many
# cubes are left in the active state after the sixth cycle?
def part1(inp: str, cycles: int = 6) -> int:
    # The grid is made up of active and inactive cubes. Represent this as a set
    # containing the positions of active cubes - anything not in the set is an
    # inactive cube.
    state = set()

    # treat the starting point as (0,0,0) - the position values don't actually
    # matter since the value to return is the number of cubes in a certain
    # state.
    y, z = 0, 0
    for line in inp.strip().split("\n"):
        for x, ch in enumerate(line.strip()):
            if ch == "#":
                state.add((x, y, z))
        y += 1

    for _ in range(cycles):
        print_state(state)
        state = one_round(state)

    return len(state)


def print_state(state: State3):

    min_z = min(z for x, y, z in state)
    max_z = max(z for x, y, z in state)

    for z in range(min_z, max_z + 1):
        print(f"z={z}")
        # probably an easier way to do this...
        min_y = min(y for x, y, z in state)
        max_y = max(y for x, y, z in state)
        min_x = min(x for x, y, z in state)
        max_x = max(x for x, y, z in state)
        for y in range(min_y, max_y + 1):
            s = ""
            for x in range(min_x, max_x + 1):
                if (x, y, z) in state:
                    s += "#"
                else:
                    s += "."
            print(s)
        print()
    return s


def one_round(state: State3) -> State3:
    # make a copy
    new_state = set(state)

    # The grid is infinite, but we have to consider if inactive cubes should
    # transition to active. Since the state set only tracks the active ones, we
    # can look at just the inactives who are neighbors of actives - inactives
    # not neighbors of an active can't transition.
    to_explore = {p: "#" for p in state}
    for p in state:
        for n in neighbors(p):
            if n not in to_explore:
                to_explore[n] = "."

    for p, ch in to_explore.items():
        active_neighbors = sum(1 if n in state else 0 for n in neighbors(p))
        if ch == "#" and active_neighbors not in {2, 3}:
            new_state.remove(p)
        elif ch == "." and active_neighbors == 3:
            new_state.add(p)

    return new_state
