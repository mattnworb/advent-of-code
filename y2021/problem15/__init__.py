from typing import *
import heapq

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


# basic idea here is to Dijkstra's shortest path. I spent a bunch of time
# reinventing this before I remembered it existing, but not getting very far.
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm


def find_lowest_risk(m: Map, start_pos: Position, end_pos: Position) -> int:
    # textbook approach is to store Infinity or some other sentinel value in the
    # dist dict, using Infinity makes the comparison of "is the new cost less
    # than the previously-thought cost for this node?" easy. Instead, treat the
    # position not being in the dict as meaning "cost not yet known", which
    # simplifies the part at the end for choosing the unvisited position with
    # lowest tentative cost.
    dist = {start_pos: 0}

    # heap
    queue = [(0, start_pos)]
    visited = set()

    def neighbors(p: Position) -> Iterator[Position]:
        x, y = p
        for n in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if n in m:
                yield n

    while queue:
        cost, current = heapq.heappop(queue)
        if current == end_pos:
            # can stop
            return dist[current]

        if current in visited:
            continue

        for neighbor in neighbors(current):
            if neighbor in visited:
                continue
            nd = dist[current] + m[neighbor]
            # neighbor is not in dist if we don't know any possible cost for it yet
            if neighbor not in dist or nd < dist[neighbor]:
                # print(f"current={current}, updating cost of {neighbor} to {nd}")
                dist[neighbor] = nd
            heapq.heappush(queue, (dist[neighbor], neighbor))

        visited.add(current)

    raise ValueError("cannot reach?")


def part1(inp: str):
    m = parse(inp)
    start_pos = (0, 0)
    # downside of storing m as dict is we have to find the end
    end_pos = max(m)

    return find_lowest_risk(m, start_pos, end_pos)


def expand_tile(original: Map, times: int) -> Map:
    # Your original map tile repeats to the right and downward; each time the
    # tile repeats to the right or downward, all of its risk levels are 1 higher
    # than the tile immediately up or left of it. However, risk levels above 9
    # wrap back around to 1
    newmap = {}

    # what size is the original grid?
    end = max(original)
    x_size, y_size = end[0] + 1, end[1] + 1

    for x in range(times):
        for y in range(times):
            # add each position of m to newmap
            for p, cost in original.items():
                newp = x_size * x + p[0], y_size * y + p[1]
                # after 9, wrap around to 1, 2, 3, ..., not 0
                newcost = cost + x + y
                if newcost > 9:
                    newcost -= 9
                newmap[newp] = newcost

    return newmap


def part2(inp: str):
    m = parse(inp)
    m = expand_tile(m, 5)

    start_pos = (0, 0)
    end_pos = max(m)

    # for y in range(end_pos[1] + 1):
    #     line = ""
    #     for x in range(end_pos[0] + 1):
    #         p = x, y
    #         line += str(m[p]) if p in m else "x"
    #     print(line)

    return find_lowest_risk(m, start_pos, end_pos)
