from typing import *
from collections import defaultdict
import heapq

# You ask the device for a heightmap of the surrounding area (your puzzle
# input). The heightmap shows the local area from above broken into a grid; the
# elevation of each square of the grid is given by a single lowercase letter,
# where a is the lowest elevation, b is the next-lowest, and so on up to the
# highest elevation, z.

# Also included on the heightmap are marks for your current position (S) and the
# location that should get the best signal (E). Your current position (S) has
# elevation a, and the location that should get the best signal (E) has
# elevation z.

# You'd like to reach E, but to save energy, you should do it in as few steps as
# possible. During each step, you can move exactly one square up, down, left, or
# right. To avoid needing to get out your climbing gear, the elevation of the
# destination square can be at most one higher than the elevation of your
# current square; that is, if your current elevation is m, you could step to
# elevation n, but not to elevation o. (This also means that the elevation of
# the destination square can be much lower than the elevation of your current
# square.)

# ...

# What is the fewest steps required to move from your current position to the
# location that should get the best signal?


# ----

# isn't this like 2021 day 15 again, with Dijkstra?

# lets try A*

Node = tuple[int, int]


def parse_into_height_map(inp) -> Tuple[Dict[Node, int], Node, Node]:
    lines = inp.split("\n")
    max_y = len(lines)
    max_x = len(lines[0])
    height: Dict[Node, int] = {}
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == "S":
                start = x, y
            elif ch == "E":
                end = x, y
            else:
                height[x, y] = ord(ch) - 96
    height[start] = 1
    height[end] = 26
    return height, start, end


def build_graph(height: Dict[Node, int]) -> Dict[Node, List[Node]]:
    # build the graph: graph[(x,y)] is a list of positions you can move to from
    # (x,y). if you can move from A to B it does not imply you can move from B
    # to A
    graph: Dict[Node, List[Node]] = defaultdict(list)
    for p in height:
        for neighbor in [
            (p[0], p[1] - 1),
            (p[0], p[1] + 1),
            (p[0] - 1, p[1]),
            (p[0] + 1, p[1]),
        ]:
            if neighbor in height:  # checking if neighbor is in grid
                # the elevation of the destination square can be at most one
                # higher than the elevation of your current square
                if height[neighbor] - height[p] <= 1:
                    graph[p].append(neighbor)
    return graph


def solve(
    height: Dict[Node, int], graph: Dict[Node, List[Node]], start: Node, end: Node
) -> Optional[int]:
    # now we search
    def h(n: Node) -> int:
        return abs(n[0] - end[0]) + abs(n[1] - end[1])

    open_set = [(start, h(start))]  # heap

    # g_score[node] is the cost of the cheapest path from start to node that we
    # know of so far
    g_score = {start: 0}
    # f_score[node] = g_score[node] + h(node). "fScore[n] represents our current
    # best guess as to how cheap a path could be from start to finish if it goes
    # through n."
    f_score = {start: h(start)}

    while open_set:
        current, _ = heapq.heappop(open_set)
        if current == end:
            # done
            return g_score[current]

        for neighbor in graph[current]:
            score = g_score[current] + 1  # cost of each move is 1
            # 'not in g_score' test is because we are only recording scores
            # we've found, not an initial state of infinity for each node
            if neighbor not in g_score or score < g_score[neighbor]:
                # this path is better than any previous one
                g_score[neighbor] = score
                f_score[neighbor] = score + h(neighbor)
                # TODO: in 2021 day 15, I had to do some tricks to deal with
                # duplicate entries in the heap for a given niehgbor, but not
                # here ... not sure why?
                heapq.heappush(open_set, (neighbor, h(neighbor)))

    # oops
    return None


def part1(inp: str):
    height, start, end = parse_into_height_map(inp)
    graph = build_graph(height)
    return solve(height, graph, start, end)


def part2(inp: str):
    height, _, end = parse_into_height_map(inp)
    graph = build_graph(height)

    # What is the fewest steps required to move starting from any square with
    # elevation a to the location that should get the best signal?
    fewest = -1
    candidates = list(filter(lambda n: height[n] == 1, height))
    for ix, start in enumerate(candidates):
        steps = solve(height, graph, start, end)
        if steps is not None and (steps < fewest or fewest == -1):
            fewest = steps
        if (ix + 1) % 100 == 0:
            print(f"tested {ix+1} of {len(candidates)} candidates")
    return fewest
