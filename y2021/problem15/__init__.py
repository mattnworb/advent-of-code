from typing import *

Position = Tuple[int, int]  # (x, y)
Path = Tuple[Position, ...]
Map = Dict[Position, int]


def parse(inp: str) -> Map:
    lines = inp.split("\n")
    return {
        (x, y): int(lines[y][x])
        for y in range(len(lines))
        for x in range(len(lines[y]))
    }


# def total_risk(m: Map, path: Path) -> int:
#     # ignore starting point
#     return sum(int(m[y][x]) for x, y in path[1:])


# basic idea here is to Djikstra's shortest path. I spent a bunch of time
# reinventing this before I remembered it existing, but not getting very far.
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm


def find_lowest_risk(m: Map, start_pos: Position, end_pos: Position) -> int:
    unvisited = set(m.keys())
    visited: Set[Position] = set()
    infinity = -1
    # textbook approach is to store Infinity or some other sentinel value in the
    # dist dict, using Infinity makes the comparison of "is the new cost less
    # than the previously-thought cost for this node?" easy. Instead, treat the
    # position not being in the dict as meaning "cost not yet known", which
    # simplifies the part at the end for choosing the unvisited position with
    # lowest tentative cost.
    dist = {start_pos: 0}

    def neighbors(p: Position) -> Iterator[Position]:
        x, y = p
        for n in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if n in m:
                yield n

    current = start_pos
    while len(unvisited) > 0:
        for neighbor in neighbors(current):
            if neighbor in unvisited:
                nd = dist[current] + m[neighbor]
                # neighbor is not in dist if we don't know any possible cost for it yet
                if neighbor not in dist or nd < dist[neighbor]:
                    # print(f"current={current}, updating cost of {neighbor} to {nd}")
                    dist[neighbor] = nd

        if current == end_pos:
            # can stop
            return dist[end_pos]

        visited.add(current)
        unvisited.remove(current)

        # select next node - unvisited with smallest dist
        possible_next = list(filter(lambda p: p in unvisited and p in dist, unvisited))
        current = min(possible_next, key=lambda p: dist[p])
    raise ValueError("cannot reach?")


def part1(inp: str):
    m = parse(inp)
    start_pos = (0, 0)

    # downside of storing m as dict is we have to find the end
    end_pos = start_pos
    for p in m:
        if p[0] > end_pos[0] or p[1] > end_pos[1]:
            end_pos = p
    # what moves can i make?
    # if can_move_up(m,pos):

    return find_lowest_risk(m, start_pos, end_pos)


def part2(inp: str):
    pass
