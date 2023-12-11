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


def parse_input(inp: str) -> Tuple[Map, Position]:
    map: Map = {}
    start: Position = (0, 0)
    for y, line in enumerate(inp.split("\n")):
        for x, ch in enumerate(line):
            map[(x, y)] = ch
            if ch == "S":
                start = (x, y)
    return map, start


def expand_loop(map: Map, start: Position) -> Set[Position]:
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

    return loop


def part1(inp: str):
    map, start = parse_input(inp)
    s_pipe = figure_out_start(map, start)
    map[start] = s_pipe

    loop = expand_loop(map, start)

    # we don't need to actually walk through the loop and count steps -
    # definitionally in a loop where each piece has two connections, the
    # furthest point has to be length/2 steps away (and the loop length has to
    # be even).
    assert len(loop) % 2 == 0
    return len(loop) // 2


def non_loop_neighbors(
    map: Map, loop: Set[Position], pos: Position
) -> Iterator[Position]:
    x, y = pos

    for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        p2 = x + d[0], y + d[1]
        if p2 in map and p2 not in loop:
            yield p2


# for any position, find the set of all neighbors (and those neighbor's neighbors, etc) until we hit either a wall or the loop
def expand_region(map: Map, region: Set[Position], loop: Set[Position], pos: Position):
    if pos in loop:
        return set()

    ns = set(non_loop_neighbors(map, loop, pos))

    new_region = region | ns

    if region == new_region:
        return region

    for neighbor in ns:
        new_region |= expand_region(map, new_region, loop, neighbor)

    return new_region


def on_border(map: Map, pos: Position) -> bool:
    if pos[0] == 0 or pos[1] == 0:
        return True

    max_pos = max(map)

    if pos[0] == max_pos[0] or pos[1] == max_pos[1]:
        return True

    return False


def part2(inp: str):
    # (map - loop) gives the set of tiles which *could* be enclosed
    #
    # keep a few sets:
    # - candidates = map - loop
    # - inside (enclosed)
    # - outside (not encloosed)
    #
    # for each tile in the candidates set:
    # - if any of its neighbors are in the outside set, mark it as outside
    # - add current + its neighbors to a queue
    # - for each in queue:
    #   - if the node is on a border - mark whole thing as outside
    #   - if node is in loop - stop
    #   - otherwise add next connections to queue
    # - when queue is empty and didn't mark as outside - mark as inside
    map, start = parse_input(inp)
    s_pipe = figure_out_start(map, start)
    map[start] = s_pipe

    loop = expand_loop(map, start)

    # each position can be in one of three sets:
    # - the loop
    # - outside the loop (not enclosed)
    # - anything else is enclosed / inside the loop

    candidates = map.keys() - loop

    outside: Set[Position] = set()
    inside: Set[Position] = set()
    for node in candidates:
        # build a set of this node and all the other non-loop positions it is
        # neighbors of, stopping at the borders of the map. if any of the
        # positions in that set touch a border, the whole set is moved to
        # "outside"

        if node in outside or node in loop:
            continue

        region = expand_region(map, {node}, loop, node)

        if any(on_border(map, p) for p in region):
            outside |= region
        else:
            inside |= region

    return len(inside)
