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

    # First approach I took here was to attempt to populate a sparse grid to
    # note every (x, y) position where a sensor is, where the beacons are, and
    # the positions that cannot contain a beacon. This works well for the
    # examples but is incredibly too slow for the actual input, since some
    # distances are on the order of 300,000, meaning points_within() returns
    # maybe around a million points to mark (times each sensor/beacon pair).
    #
    # Second approach was to walk through just the row we are interested in,
    # figure out the left-most and right-most positions worth checking (where we
    # could possibly rule out some beacons), and then for each position between
    # them, test if that position falls within the sensor-beacon range for any
    # sensor. This works better for the input but is still pretty slow: ~13
    # second execution time for Part 1.
    #
    # Third approach which might be much faster - combine the best parts of the
    # two above - for each sensor-beacon pair, just figure out which (x, y)
    # positions *in the row we care about* have a distance <= the manhattan
    # distance of the pair. Can do some math to figure out where the left and
    # right bounds are and then fill in the spots in between (where there is not
    # a beacon or sensor already).

    sensors = set()
    beacons = set()
    sensor_to_beacon = {}
    # distances = []

    not_beacons: Set[Point] = set()

    for sensor, beacon in parse(inp):
        sensors.add(sensor)
        beacons.add(beacon)
        sensor_to_beacon[sensor] = beacon
        # distances.append(distance(sensor, beacon))

    for sensor, beacon in sensor_to_beacon.items():
        d = distance(sensor, beacon)

        # based on the radius `d`, what is the edge of where beacons cannot be for this sensor *in this row* ?
        leftover_d = d - abs(y - sensor[1])
        left_x = sensor[0] - leftover_d
        right_x = sensor[0] + leftover_d

        # nothing in between left_x and right_x can be a beacon
        for x in range(left_x, right_x + 1):
            p = (x, y)
            # skip positions where sensors and beacons are
            if p not in sensors and p not in beacons:
                not_beacons.add(p)

    return len(not_beacons)


def part2(inp: str):
    pass
