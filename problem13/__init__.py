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
# example1:
# inp = "7,13,x,x,59,x,31,19"
# d = {0:7, 1:13, 4:59, 6:31, 7:19}
# answer = 1068781

# t + 7 == 19a
# t + 6 == 31b
# t + 4 == 59c
# t + 1 == 13d
# t + 0 == 7e


# (t + 0) % 7 == 0
# (t + 1) % 13 == 0
# (t + 4) % 59 == 0
# (t + 6) % 31 == 0
# (t + 7) % 19 == 0

# can we use division?
# (t + 0) / 7 == 0
# (t + 1) / 13 == 0
# (t + 4) / 59 == 0
# (t + 6) / 31 == 0
# (t + 7) / 19 == 0

# t / 7 == (t + 1) / 13
# t = 7 *(t/13 + 1/13)
# t = (7/13)t + 7/13
# t - (7/13)t = 7/13
# (6/13)t = 7/13
# 6t = 7
# t = 7/6

# t = 7 * (t+1) / 13
# t = (7t + 7) / 13
# 13t = 7t + 7
# 6t = 7
#  t = 7/6

#####################################################################################
# Ok smart thinking from here
# input like "7,13":
# first t is ( 77,  78)       = 78 = 13 * (13 % 7)
# next is    (168, 169)
# next is    (259, 169)
#
# difference between cycles (in the first position) is 91 ... which is 7 * 13
#
# what formula gives us these values?
#
# input like "7,15":
# - ( 14,  15)             15 = 15 * (15 % 7)
# - (119, 120)
# - (224, 225)
# - (329, 330)
#
# 105 between cycles ... which is 7 * 15
#
# seems like if we have N buses, we can break it down by finding the cycle for
# the first 2, then using that with the 3rd, etc?
#
#
# ok now try with bigger gaps: "7,x,13"
# - ( 63,  65)             65 = 13 * (13 % 7 - 1) = 13 * 5
# - (154, 156)
# - (245, 247)
# - (336, 338)
# cycle: 91 again!! which is 7*13
#
# input: "7,x,17"
# - ( 49,  51)             51 = 17 * (17 % 7 - 1) = 17 * 2 .... this one is wrong and doesn't fit
# - (168, 170)                                                  should be 17 * 3
# - (287, 289)
# - (406, 408)
# cycle: 119 = 7 * 17
#
# input: "7,x,19"
# - (112, 114)            114 = 19 * (19 % 7 - 1) = 19 * 4 ... wrong, should be 19 * 6
# - (245, 247)
# - (378, 380)
#
#
# General pattern seems to be: cycle = b0 * b1
#  but how to find the first match?
# I thought the equation would be - take the larger element (n), and find: n * (n % m - (i-1))
# but this doesn't fit always


def is_valid(t: int, buses: Dict[int, int]) -> bool:

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


def part2_find_min_answer_gen(buses: Dict[int, int]):
    max_bus = -1
    for ix, bus in buses.items():
        if bus > max_bus:
            max_bus = bus
            max_ix = ix

    t = max_bus

    while True:
        if is_valid(t - max_ix, buses):
            yield [t - offset for offset in sorted(buses.keys(), reverse=True)]
        t += max_bus
