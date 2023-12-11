from typing import *


# Find the single giant loop starting at S. How many steps along the loop does
# it take to get from the starting position to the point farthest from the
# starting position?
#
# -----------------
#
# thoughts:
# - counting the distance in steps from S is easy enough
# - furthest distance is position where the num steps is higher than any
#   neighbor
# - we probably have to filter the map first to find the "single giant loop" so
#   we don't go down any one-way paths and mistakenly count them as "the point
#   farthest"
Position = Tuple[int, int]
Map = Dict[Position, str]

connects_north = {"|", "L", "J"}
connects_south = {"|", "7", "F"}
connects_west = {"-", "J", "7"}
connects_east = {"-", "L", "F"}


def connections(map: Map, pos: Position) -> Set[Position]:
    c = set()
    x, y = pos

    this_pipe = map[pos]

    # north
    if this_pipe in connects_north and map.get((x, y - 1), None) in connects_south:
        c.add((x, y - 1))

    # south
    if this_pipe in connects_south and map.get((x, y + 1), None) in connects_north:
        c.add((x, y + 1))

    # west
    if this_pipe in connects_west and map.get((x - 1, y), None) in connects_east:
        c.add((x - 1, y))

    # right
    if this_pipe in connects_east and map.get((x + 1, y), None) in connects_west:
        c.add((x + 1, y))

    return c


def figure_out_start(map: Map, pos: Position):
    possible = set()
    x, y = pos

    # could S have a north connection?
    if map.get((x, y - 1), None) in connects_south:
        possible = connects_north

    # south?
    if map.get((x, y + 1), None) in connects_north:
        possible = possible & connects_south if possible else connects_south

    # west?
    if map.get((x - 1, y), None) in connects_east:
        possible = possible & connects_west if possible else connects_west

    # east?
    if map.get((x + 1, y), None) in connects_west:
        possible = possible & connects_east if possible else connects_east

    assert len(possible) == 1
    return next(iter(possible))


def part1(inp: str):
    # parse input
    map: Map = {}
    start: Position = (0, 0)
    for y, line in enumerate(inp.split("\n")):
        for x, ch in enumerate(line):
            map[(x, y)] = ch
            if ch == "S":
                start = (x, y)

    # print(f"S is at {start}")

    s_pipe = figure_out_start(map, start)
    # print(f"S must be: {s_pipe}")

    map[start] = s_pipe

    # figure out what the loop's positions are by walking out from each of the
    # connections of the starting point
    #
    # another approach here would be to walk from the starting point with two
    # pointers, moving "away" in each step. i.e. if the piece is a | and we come
    # from the south, we know we have to go to the north in the next step. count
    # the number of steps until the two pointers are at the same position.
    loop = {start}
    queue: List[Position] = list(connections(map, start))

    while queue:
        cur = queue.pop()
        if cur not in loop:
            loop.add(cur)
            conns = connections(map, cur)
            for conn in conns:
                queue.append(conn)

    # print(f"found loop (size={len(loop)}): {loop}")

    # we don't need to actually walk through the loop and count steps -
    # definitionally in a loop where each piece has two connections, the
    # furthest point has to be length/2 steps away (and the loop length has to
    # be even).
    assert len(loop) % 2 == 0
    return len(loop) // 2


# hi


def part2(inp: str):
    pass
