from typing import *

from math import lcm


def parse_buses(line: str) -> Dict[int, int]:
    return {ix: int(b) for ix, b in enumerate(line.strip().split(",")) if b != "x"}


def part1(start_t: int, buses: Dict[int, int]) -> Tuple[int, int]:
    min_t = -1
    min_bus = -1
    for bus in buses.values():
        t = next_time(start_t, bus)
        if min_t == -1 or t < min_t:
            min_t = t
            min_bus = bus
    return min_t - start_t, min_bus


def next_time(t: int, bus: int) -> int:
    return t + (bus - (t % bus))


def part2_sieve(buses: Dict[int, int]) -> int:
    offsets = sorted(buses.keys())

    # start walking through possible t's by strides that are = buses[0]
    t = offsets[0]
    stride = buses[0]

    for offset in offsets[1:]:
        while (t + offset) % buses[offset] != 0:
            t += stride
        # print(
        #     f"found match at t={t} for position={offset} bus_id={buses[offset]} stride={stride}"
        # )
        # for o in offsets:
        #     print(f"\tt={t+o} o={o} bus_id={buses[o]} valid={(t + o) % buses[o] == 0}")

        # increase the stride by lcm(stride, buses[offset])
        #
        # Since we know that the offsets are prime, this is just a
        # multiplication, but we use math.lcm below to be safe.
        #
        # intuition here: if we have found a t that works for the first 2 buses, e.g.:
        # input: "17,x,13,19"
        # t=102 % 17 == 0
        # t=103 ...
        # t=104 % 13 == 0   (t=102+2)
        #
        # this will next repeat at t=102 + lcm(17, 13) = 102 + 221
        # t=323 % 17 == 0
        # t=324 ...
        # t=325 % 13 == 0   (t=323+2)
        #
        # This means that each time we move to a new offset and buses[offset],
        # we are increasing the stride even more, guaranteeing that we land at
        # values of t that match all of buses[0:offset].
        stride = lcm(stride, buses[offset])

    return t
