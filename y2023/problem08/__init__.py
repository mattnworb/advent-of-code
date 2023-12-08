from typing import *


def part1(inp: str):
    lines = inp.split("\n")
    moves = lines[0]

    nodes: Dict[str, Tuple[str, str]] = {}

    for line in lines[2:]:
        src, dst = line.split(" = ")
        # assume the nodes are always 3 chars in length
        assert len(src) == 3
        assert len(dst) == 10
        nodes[src] = (dst[1:4], dst[6:9])

    pos = "AAA"

    steps = 0
    while pos != "ZZZ":
        # we run through all the moves before checking if we are at ZZZ
        # - is that right?
        for move in moves:
            steps += 1
            if move == "R":
                pos = nodes[pos][1]
            elif move == "L":
                pos = nodes[pos][0]
            else:
                raise ValueError("unknown move " + move)

    return steps


# Simultaneously start on every node that ends with A. How many steps does it
# take before you're only on nodes that end with Z?
def part2(inp: str):
    lines = inp.split("\n")
    moves = lines[0]
    assert all(ch == "R" or ch == "L" for ch in moves)

    nodes: Dict[str, Tuple[str, str]] = {}

    for line in lines[2:]:
        src, dst = line.split(" = ")
        # assume the nodes are always 3 chars in length
        assert len(src) == 3
        assert len(dst) == 10
        nodes[src] = (dst[1:4], dst[6:9])

    start_state = set(filter(lambda node: node.endswith("A"), nodes.keys()))
    end_state = set(filter(lambda node: node.endswith("Z"), nodes.keys()))

    positions = start_state
    steps = 0
    while True:
        for move in moves:
            steps += 1
            next_state = set()
            for node in positions:
                next_state.add(nodes[node][0] if move == "L" else nodes[node][1])

            positions = next_state
            if positions == end_state:
                return steps
    # return steps
