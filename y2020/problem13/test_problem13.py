from . import *


def test_part1_example():
    assert part1(939, parse_buses("7,13,x,x,59,x,31,19")) == (5, 59)


def test_next_time():
    assert next_time(939, 59) == 944
    assert next_time(939, 7) == 945


def test_part2_sieve():
    assert part2_sieve(parse_buses("17,x,13,19")) == 3417
    assert part2_sieve(parse_buses("7,13,x,x,59,x,31,19")) == 1068781
    assert part2_sieve(parse_buses("17,x,13,19")) == 3417
    assert part2_sieve(parse_buses("67,7,59,61")) == 754018
    assert part2_sieve(parse_buses("67,x,7,59,61")) == 779210
    assert part2_sieve(parse_buses("67,7,x,59,61")) == 1261476
    assert part2_sieve(parse_buses("1789,37,47,1889")) == 1202161486
