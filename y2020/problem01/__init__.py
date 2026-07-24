import itertools
from functools import reduce
from typing import List, Optional, Tuple


def find_sum_product(nums: list[int], length: int, goal: int) -> int | None:
    for c in itertools.combinations(nums, length):
        if sum(c) == goal:
            return reduce(lambda a, b: a * b, c)
    return None
