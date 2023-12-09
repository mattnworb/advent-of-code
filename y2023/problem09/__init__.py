from typing import *


def calculate_next_value(nums: List[int]) -> int:
    # initially was checking if the sum was 0 here, but that can break if the
    # list contains postivie and negative numbers
    if all(n == 0 for n in nums):
        return 0

    diff_between_values = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

    return nums[-1] + calculate_next_value(diff_between_values)


# "Analyze your OASIS report and extrapolate the next value for each history.
# What is the sum of these extrapolated values?"
def part1(inp: str):
    seqs: List[List[int]] = []
    for line in inp.split("\n"):
        seqs.append(list(map(int, line.split())))

    next_vals = list(map(calculate_next_value, seqs))
    return sum(next_vals)


def calculate_prev_value(nums: List[int]) -> int:
    if all(n == 0 for n in nums):
        return 0

    diff_between_values = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

    return nums[0] - calculate_prev_value(diff_between_values)


def part2(inp: str):
    seqs: List[List[int]] = []
    for line in inp.split("\n"):
        seqs.append(list(map(int, line.split())))

    next_vals = list(map(calculate_prev_value, seqs))
    return sum(next_vals)
