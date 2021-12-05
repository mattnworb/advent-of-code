from typing import *
from collections import Counter

# tuple where index 0 = x, 1 = y
Point = Tuple[int]


def points_in_line(p1: Point, p2: Point) -> Iterable[Point]:
    assert is_horizontal_or_vertical(p1, p2)
    (x1, y1), (x2, y2) = p1, p2  # unpack for readability
    if x1 == x2:
        # input can be in either direction - fix order
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            yield x1, y
    else:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            yield x, y1


def is_horizontal_or_vertical(p1: Point, p2: Point) -> bool:
    return p1[0] == p2[0] or p1[1] == p2[1]


def parse_points(line: str) -> Tuple[Point]:
    # value is like: x1,y1 -> x2,y2
    left, right = line.split(" -> ")
    p1 = tuple(map(int, left.split(",")))
    p2 = tuple(map(int, right.split(",")))
    return p1, p2


def part1(inp: str):
    lines = inp.split("\n")

    grid: Counter[Point] = Counter()

    for line in lines:
        p1, p2 = parse_points(line)
        if is_horizontal_or_vertical(p1, p2):
            for p in points_in_line(p1, p2):
                grid[p] += 1

    # find all points in grid where >= 2 lines overlap
    ans = 0
    for p, count in grid.items():
        if count >= 2:
            ans += 1
    return ans


def part2(inp: str):
    pass
