from typing import *
import string
from collections import defaultdict

Path = Tuple[str, ...]
Graph = Dict[str, List[str]]


def part1(inp: str):
    graph: Graph = defaultdict(list)
    for line in inp.split("\n"):
        a, b = line.split("-")
        # graph is in both directions
        graph[a].append(b)
        graph[b].append(a)

    # Your goal is to find the number of distinct paths that start at start, end
    # at end, and don't visit small caves more than once. There are two types of
    # caves: big caves (written in uppercase, like A) and small caves (written
    # in lowercase, like b). It would be a waste of time to visit any small cave
    # more than once, but big caves are large enough that it might be worth
    # visiting them multiple times. So, all paths you find should visit small
    # caves at most once, and can visit big caves any number of times.

    paths: Set[Path] = set()

    cur_path: Path = ("start",)

    find_all_paths(paths, graph, cur_path)

    return len(paths)


def is_small(cave: str) -> bool:
    return all(c in string.ascii_lowercase for c in cave)


def legit_next_moves(graph: Graph, path: Path) -> Iterator[str]:
    location = path[-1]
    if location not in graph:
        return
    for cave in graph[location]:
        # can move if cave is big, or is small but not yet visited
        if not is_small(cave) or cave not in path:
            yield cave


def find_all_paths(paths: Set[Path], graph: Graph, cur_path: Path):
    next_moves = list(legit_next_moves(graph, cur_path))
    if len(next_moves) == 0:
        # abort this path
        return
    for next_cave in next_moves:
        # should probably check if the previous cave was the same as next_cave to avoid loops
        new_path = cur_path + (next_cave,)
        if next_cave == "end":
            paths.add(new_path)
        else:
            find_all_paths(paths, graph, new_path)


def part2(inp: str):
    pass
