from typing import *
import re

parse_pattern = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)

Point = Tuple[int, int]


class Grid:
    def __init__(self):
        self.grid = {}

    def add(self, p: Point, ch: str) -> None:
        self.grid[p] = ch

    def __getitem__(self, p: Point) -> str:
        return self.grid[p]

    def get_row(self, y: int) -> Iterator[str]:
        """Iterate over every item in the row, from left to right"""
        # for p, ch in self.grid.items():
        #     if p[1] == y:
        #         yield ch

        for x in range(self.minx(), self.maxx() + 1):
            p = (x, y)
            yield self.grid[p] if p in self.grid else "."

    # TODO: maybe compute these on each write
    def maxx(self):
        return max(p[0] for p in self.grid)

    def minx(self):
        return min(p[0] for p in self.grid)

    def maxy(self):
        return max(p[1] for p in self.grid)

    def miny(self):
        return min(p[1] for p in self.grid)

    def __contains__(self, p: Point) -> bool:
        return p in self.grid


def distance(a: Point, b: Point) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# TODO this is too inefficient for a distance like 325168
def points_within(p: Point, distance: int) -> Iterator[Point]:
    """Return an iterator of all the Points within a manhattan distance of
    `distance` of the point `p`."""

    print(f"points_within({p}, {distance})")
    # mark every point from (x, y) that has distance <= `distance` from it
    for d in range(1, distance + 1):
        # four cardinal directions
        # this is missing combined moves
        yield p[0] + d, p[1]
        yield p[0] - d, p[1]
        yield p[0], p[1] + d
        yield p[0], p[1] - d

        # go left A times, up B times where A + B == D
        # go left A times, down B times where A + B == D
        # go right A times, up B times where A + B == D
        # go right A times, down B times where A + B == D
        for a in range(1, d):
            b = d - a
            yield p[0] + a, p[1] + b
            yield p[0] + a, p[1] - b
            yield p[0] - a, p[1] + b
            yield p[0] - a, p[1] - b


def parse(inp: str) -> List[Tuple[Point, Point]]:
    items = []
    for line in inp.split("\n"):
        m = parse_pattern.fullmatch(line)
        assert m is not None, f"line did not match regex: {line}"
        sensorx, sensory, beaconx, beacony = map(
            int, [m.group(1), m.group(2), m.group(3), m.group(4)]
        )
        pair = (sensorx, sensory), (beaconx, beacony)
        items.append(pair)
    return items


def part1(inp: str, y=2000000) -> int:
    grid = Grid()
    for sensor, beacon in parse(inp):
        grid.add(sensor, "S")
        grid.add(beacon, "B")

        for p in points_within(sensor, distance(sensor, beacon)):
            if p not in grid:
                grid.add(p, "#")

    return len([n for n in grid.get_row(y) if n == "#"])


def part2(inp: str):
    pass
