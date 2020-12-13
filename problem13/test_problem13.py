from problem13 import *


def test_part1_example():
    assert part1(939, [7, 13, 59, 31, 19]) == (5, 59)


def test_next_time():
    assert next_time(939, 59) == 944
    assert next_time(939, 7) == 945


def test_part2_is_valid():
    assert is_valid(1068781, "7,13,x,x,59,x,31,19") == True


def test_part2_example1():
    assert part2_find_min_answer("939\n7,13,x,x,59,x,31,19") == 1068781
