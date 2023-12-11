from typing import *
from itertools import combinations

Position = Tuple[int, int]


def expand(s: List[str], multiplier=2) -> Set[Position]:
    # rather than storing the whole map, and then mutating it to insert rows and
    # columns, just store the positions of the galaxies, and then figure out how
    # to mutate each one to add some number to the x and y coordinates each
    # based on how many empty rows or columns come "before" it.

    # read in the positions of the galaxies
    g = set()
    for y, line in enumerate(s):
        for x, ch in enumerate(line):
            if ch == "#":
                g.add((x, y))

    # TODO: loop over g less
    g_xs = set(p[0] for p in g)
    g_ys = set(p[1] for p in g)

    missing_x = set(range(max(g_xs))) - g_xs
    missing_y = set(range(max(g_ys))) - g_ys

    new_g = set()

    for galaxy in g:
        # transpose
        empty_rows_before = len([r for r in missing_y if r < galaxy[1]])
        empty_cols_before = len([c for c in missing_x if c < galaxy[0]])
        new_g.add(
            (
                galaxy[0] + empty_cols_before * (multiplier - 1),
                galaxy[1] + empty_rows_before * (multiplier - 1),
            )
        )

    return new_g


def distance(a: Position, b: Position) -> int:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def part1(inp: str):
    lines = inp.split("\n")
    galaxies = expand(lines)

    total = 0
    for pair in combinations(galaxies, 2):
        total += distance(pair[0], pair[1])
    return total


def part2(inp: str):
    lines = inp.split("\n")
    galaxies = expand(lines, multiplier=1000000)

    total = 0
    for pair in combinations(galaxies, 2):
        total += distance(pair[0], pair[1])
    return total
