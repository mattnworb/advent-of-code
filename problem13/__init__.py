from typing import *


def part1(start_t: int, buses: List[int]) -> Tuple[int, int]:
    min_t = -1
    min_bus = -1
    for bus in buses:
        t = next_time(start_t, bus)
        if min_t == -1 or t < min_t:
            min_t = t
            min_bus = bus
    return min_t - start_t, min_bus


def next_time(t: int, bus: int) -> int:
    return t + (bus - (t % bus))


### part 2


def is_valid(t: int, buses: Dict[int, int]) -> bool:
    # example1:
    # inp = "7,13,x,x,59,x,31,19"
    # d = {0:7, 1:13, 4:59, 6:31, 7:19}
    # answer = 1068781
    return all((t + offset) % bus == 0 for offset, bus in buses.items())


def parse_p2_input(line: str) -> Dict[int, int]:
    return {ix: int(b) for ix, b in enumerate(line.strip().split(",")) if b != "x"}


# Naive attempt, try each multiple of the max bus
def part2_find_min_answer(inp: str) -> int:
    i = inp.split("\n")
    buses = parse_p2_input(i[1])

    max_bus = -1
    for ix, bus in buses.items():
        if bus > max_bus:
            max_bus = bus
            max_ix = ix

    t = max_bus
    while True:
        if is_valid(t - max_ix, buses):
            return t - max_ix
        t += max_bus
