from typing import List, Tuple, Optional

import itertools
from functools import reduce


def find_sum_product(nums: List[int], length: int, goal: int) -> Optional[int]:
    for c in itertools.combinations(nums, length):
        if sum(c) == goal:
            return reduce(lambda a, b: a * b, c)
    return None
