from . import *

nums = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_part1_example():
    assert find_not_sum_pair(nums, preamble_length=5) == 127


def test_part2_example():
    first_invalid = find_not_sum_pair(nums, preamble_length=5)
    window = find_contiguous_sum(nums, first_invalid)
    output = min(window) + max(window)
    assert output == 62
