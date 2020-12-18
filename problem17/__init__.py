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

Position = Tuple[int, int, int]
# State = Dict[Position, str]


class State(object):
    def __init__(self, initial_state: Set[Position] = None):
        self.state = initial_state or set()

    def set_state(self, p: Position, active: bool):
        if active:
            self.state.add(p)
        elif p in self.state:
            self.state.remove(p)

    def get_state(self, p: Position) -> bool:
        return p in self.state

    # def get_positions(self) -> Set[Position]:
    #     positions = set(self.state.keys())
    #     # union
    #     return positions | set(n for p in positions for n in neighbors(p))

    def copy(self) -> "State":
        return State(initial_state=set(self.state))

    def active_positions(self) -> Set[Position]:
        return self.state

    def __repr__(self):
        return f"len={len(self.state)} " + repr(self.state)

    def viz(self):
        min_z = min(z for x, y, z in self.state)
        max_z = max(z for x, y, z in self.state)
        s = ""
        for z in range(min_z, max_z + 1):
            s += f"z={z}"
            min_y = min(y for x, y, z in self.state)
            max_y = max(y for x, y, z in self.state)
            min_x = min(x for x, y, z in self.state)
            max_x = max(x for x, y, z in self.state)
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    if self.get_state((x, y, z)):
                        s += "#"
                    else:
                        s += "."
                s += "\n"
            s += "\n"
        return s
        # x, y = min((x, y) for x, y, z1 in self.state if z1 == z)


def neighbors(p: Position) -> Iterator[Position]:  # Generator[int, None, None]:
    r = range(-1, 2)
    for x in r:
        for y in r:
            for z in r:
                if not (x == y == z == 0):
                    yield p[0] + x, p[1] + y, p[2] + z


# Starting with your given initial configuration, simulate six cycles. How many
# cubes are left in the active state after the sixth cycle?
def part1(inp: str, cycles: int = 6) -> int:
    # default positions to inactive
    state = State()  #: State = defaultdict(lambda: ".")

    # treat the starting point as (0,0,0) - the values don't actually matter since the answer to return is the number of cubes in a certain state
    y, z = 0, 0
    for line in inp.strip().split("\n"):
        for x, ch in enumerate(line.strip()):
            state.set_state((x, y, z), ch == "#")
        y += 1

    for _ in range(cycles):
        print(state.viz())
        state = one_round(state)

    return len(state.active_positions())


def one_round(state: State) -> State:
    new_state = state.copy()

    # the rules say all inactive cubes have to be looked at, but also, they are
    # an unlimited amount. is it enough to just look at each key?

    # since we use a defaultdict, simply looking at all the neighbors changes
    # the contents/size of state - so make a copy of the keys first
    # keys = list(state.keys())
    # for p in keys:  # , ch in state.items():
    #     ch = state[p]
    #     active_neighbors = sum(1 if state[n] == "#" else 0 for n in neighbors(p))
    #     if state[p] == "#" and active_neighbors not in {2, 3}:
    #         new_state[p] = "."
    #     elif state[p] == "." and active_neighbors == 3:
    #         new_state[p] = "#"

    actives = state.active_positions()
    to_explore = {p: "#" for p in actives}
    # | set(n for p in actives for n in neighbors(p))
    for p in actives:
        for n in neighbors(p):
            if n not in to_explore:
                to_explore[n] = "."

    for p, ch in to_explore.items():
        active_neighbors = sum(1 if state.get_state(n) else 0 for n in neighbors(p))
        if ch == "#" and active_neighbors not in {2, 3}:
            new_state.set_state(p, False)
        elif ch == "." and active_neighbors == 3:
            new_state.set_state(p, True)

    return new_state
