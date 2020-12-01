from typing import List, Tuple, Optional


def find_pair(nums: List[int], goal: int) -> Optional[Tuple[int, int]]:
    for x in nums:
        for y in nums:
            if x == y:
                continue
            if x + y == goal:
                return (x, y) if x < y else (y, x)
    return None
