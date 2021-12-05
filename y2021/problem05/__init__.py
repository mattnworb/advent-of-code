from typing import *
from collections import Counter

# tuple where index 0 = x, 1 = y
Point = Tuple[int, int]


def points_in_line(p1: Point, p2: Point, allow_diagonal: bool) -> Iterable[Point]:
    assert is_allowed(p1, p2, allow_diagonal)

    # unpack for readability
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        # input can be in either direction - fix order
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            yield x1, y
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            yield x, y1
    elif allow_diagonal:
        # diagonal line
        # figure out traversal order
        if x1 > x2:
            x_range = range(x1, x2 - 1, -1)
        else:
            x_range = range(x1, x2 + 1)
        if y1 > y2:
            y_range = range(y1, y2 - 1, -1)
        else:
            y_range = range(y1, y2 + 1)

        for x, y in zip(x_range, y_range):
            yield x, y


def is_allowed(p1: Point, p2: Point, allow_diagonal: bool) -> bool:
    return (
        p1[0] == p2[0]
        or p1[1] == p2[1]
        or (allow_diagonal and abs(p1[0] - p2[0]) == abs(p1[1] - p2[1]))
    )


def parse_points(line: str) -> Tuple[Point, Point]:
    # value is like: x1,y1 -> x2,y2
    left, right = line.split(" -> ")
    s1 = left.split(",", 2)
    s2 = right.split(",", 2)
    p1 = int(s1[0]), int(s1[1])
    p2 = int(s2[0]), int(s2[1])
    return p1, p2


def count_overlapping_lines(inp: str, allow_diagonal: bool) -> int:
    lines = inp.split("\n")

    grid: Counter[Point] = Counter()

    for line in lines:
        p1, p2 = parse_points(line)
        if is_allowed(p1, p2, allow_diagonal):
            for p in points_in_line(p1, p2, allow_diagonal):
                grid[p] += 1

    # find all points in grid where >= 2 lines overlap
    ans = 0
    for p, count in grid.items():
        if count >= 2:
            ans += 1
    return ans


def part1(inp: str):
    return count_overlapping_lines(inp, False)


def part2(inp: str):
    return count_overlapping_lines(inp, True)
