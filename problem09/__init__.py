from typing import List, Set
import itertools

# The first step of attacking the weakness in the XMAS data is to find the first
# number in the list (after the preamble) which is not the sum of two of the 25
# numbers before it. What is the first number that does not have this property?


def find_not_sum_pair(nums: List[int], preamble_length=25) -> int:
    for i in range(preamble_length, len(nums)):
        allowed = compute_sum_pairs(nums[i - preamble_length : i])

        if nums[i] not in allowed:
            return nums[i]

    raise ValueError("uh oh - done?")


def compute_sum_pairs(nums: List[int]) -> Set[int]:
    return set(map(lambda t: t[0] + t[1], itertools.combinations(nums, 2)))


# The final step in breaking the XMAS encryption relies on the invalid number
# you just found: you must find a contiguous set of at least two numbers in your
# list which sum to the invalid number from step 1.
# ...
# To find the encryption weakness, add together the smallest and largest number
# in this contiguous range; in this example, these are 15 and 47, producing 62.


# this is obviously unoptimized and just brute forcing, but it runs fine for an
# input of 1000 numbers
def find_contiguous_sum(nums: List[int], target: int) -> List[int]:
    for size in range(2, len(nums)):
        for n in range(0, len(nums) - size):
            window = nums[n : n + size]
            if sum(window) == target:
                return window

    raise ValueError("uh oh no sum found?!")
