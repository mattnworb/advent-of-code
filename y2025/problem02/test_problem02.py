from y2025.problem02 import *

example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def test_part1_example():
    assert part1(example) == 1227775554


def test_part2_is_invalid():
    assert part2_is_invalid(1010) == True
    assert part2_is_invalid(1011) == False


def test_part2_example():
    assert part2(example) == 4174379265
