from typing import *
import collections


def part1(inp: str) -> int:
    # keep it as strings
    nums = [line.strip() for line in inp.split("\n")]

    gamma_rate = ""
    len_line = len(nums[0])
    for n in range(len_line):
        c = collections.Counter([num[n] for num in nums])
        most_common_ch = c.most_common(1)[0][0]
        gamma_rate += most_common_ch

    # episilon rate is inverse - least common char in each pos. shortcut: if
    # most common is 1, least common must be 0
    def inverse(ch: str) -> str:
        assert ch == "0" or ch == "1"
        return "0" if ch == "1" else "1"

    episilon_rate = "".join(inverse(ch) for ch in gamma_rate)

    # the two rate are strings, convert to numbers
    return int(gamma_rate, 2) * int(episilon_rate, 2)


def oxygen_rating(nums: List[str]) -> int:
    remaining = list(nums)  # copy

    len_line = len(nums[0])
    for n in range(len_line):
        if len(remaining) == 1:
            break

        c = collections.Counter([num[n] for num in remaining])
        most_common = c.most_common(2)
        # if occurences are equal, use 1
        if most_common[0][1] == most_common[1][1]:
            most_common_ch = "1"
        else:
            most_common_ch = most_common[0][0]
        # keep only numbers that have most_common_ch in this position
        remaining = list(filter(lambda num: num[n] == most_common_ch, remaining))

    assert len(remaining) == 1

    return int(remaining[0], 2)


def co2_rating(nums: List[str]) -> int:
    remaining = list(nums)  # copy

    len_line = len(nums[0])
    for n in range(len_line):
        if len(remaining) == 1:
            break

        c = collections.Counter([num[n] for num in remaining])
        most_common = c.most_common(2)
        # if occurences are equal, use 0
        if most_common[0][1] == most_common[1][1]:
            least_common_ch = "0"
        else:
            # otherwise LEAST common
            least_common_ch = most_common[1][0]
        # keep only numbers that have least_common_ch in this position
        remaining = list(filter(lambda num: num[n] == least_common_ch, remaining))

    assert len(remaining) == 1

    return int(remaining[0], 2)


def part2(inp: str):
    nums = [line.strip() for line in inp.split("\n")]
    return oxygen_rating(nums) * co2_rating(nums)
