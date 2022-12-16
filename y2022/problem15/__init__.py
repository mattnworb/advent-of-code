from typing import *
import re

parse_pattern = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)

Point = Tuple[int, int]


def distance(a: Point, b: Point) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


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

    sensors = []
    beacons = []
    distances = []

    for sensor, beacon in parse(inp):
        sensors.append(sensor)
        beacons.append(beacon)
        distances.append(distance(sensor, beacon))

    # we don't know exactly what x positions to scan between on this row, but we know the max it can be
    x_start, x_end = (
        min([p[0] - distances[i] for i, p in enumerate(sensors)]),
        max([p[0] + distances[i] for i, p in enumerate(sensors)]),
    )

    print(f"scanning row={y} between [{x_start}, {x_end}]")
    count = 0
    for x in range(x_start, x_end + 1):
        p = x, y

        if p in beacons:
            continue

        # if the point is closer to any sensor than its beacon is, then it cannot be a beacon
        cannot_be_beacon = False
        for ix, sensor in enumerate(sensors):
            if distance(p, sensor) <= distances[ix]:
                cannot_be_beacon = True
                break

        if cannot_be_beacon:
            count += 1
            # print("cannot be beacon", p)

    return count


def part2(inp: str):
    pass
