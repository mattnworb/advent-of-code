from typing import List, Dict, Tuple, Optional, Set

import itertools
import collections

# Each of your joltage adapters is rated for a specific output joltage (your
# puzzle input). Any given adapter can take an input 1, 2, or 3 jolts lower than
# its rating and still produce its rated output joltage.
#
# In addition, your device has a built-in joltage adapter rated for 3 jolts
# higher than the highest-rated adapter in your bag. (If your adapter list were
# 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)
#
# Treat the charging outlet near your seat as having an effective joltage rating
# of 0.
#
# Since you have some time to kill, you might as well test all of your adapters.
# Wouldn't want to get to your resort and realize you can't even charge your
# device!
#
# If you use every adapter in your bag at once, what is the distribution of
# joltage differences between the charging outlet, the adapters, and your
# device?

# Originally my solution tried to find a valid chain of adapters from the input
# which would use all of them. But duh, if we use all of them, there is only one
# ordering possible, since the allowed differences of [1, 2, or 3] are all
# positive - its not like we can have adapter 5, then 3, then 6.
def solve_part1(adapters: List[int]) -> int:
    a = [0] + sorted(adapters) + [max(adapters) + 3]

    c: Dict[int, int] = {}

    for i in range(1, len(a)):
        diff = a[i] - a[i - 1]
        if diff > 3 or diff < 1:
            raise ValueError("bad input")
        if diff not in c:
            c[diff] = 1
        else:
            c[diff] += 1
    return c[1] * c[3]


# this is so ugly, find a better solution
def find_chain(adapters: List[int], chain=None, joltage=0) -> Optional[List[int]]:
    # infinite loop when input is not sorted, why?
    new_adapters = sorted(adapters) + [max(adapters) + 3]
    return _find_chain(new_adapters, chain=chain, joltage=joltage)


def _find_chain(adapters: List[int], chain=None, joltage=0) -> Optional[List[int]]:
    if len(adapters) == 0:
        print(f"done! chain is {chain}")
        return chain

    # how many adapters can connect to the current joltage?
    for adapter in adapters:
        # only diff of 1, 2, or 3 allowed
        if 0 < adapter - joltage <= 3:
            copy = list(adapters)
            copy.remove(adapter)
            print(
                f"at joltage={joltage}, trying {adapter}, remaining adapters {len(copy)}"
            )

            new_chain = [adapter] if chain is None else chain + [adapter]

            solution = _find_chain(copy, chain=new_chain, joltage=adapter)
            if solution:
                return solution

    return None


def distances(chain: List[int]) -> Dict[int, int]:
    c: Dict[int, int] = collections.Counter()

    prev = 0
    for i in range(len(chain)):
        diff = chain[i] - prev
        c[diff] += 1
        prev = chain[i]
    return c


# recursion with memoization
def part2(adapters: List[int]) -> int:
    return _part2(0, set(adapters), max(adapters), {})


def _part2(current, adapters: Set[int], end, memo) -> int:
    if (current, end) in memo:
        return memo[(current, end)]

    if current > 0 and current not in adapters:
        return 0

    if current > end:
        return 0

    if current == end:
        return 1

    c = (
        _part2(current + 1, adapters, end, memo)
        + _part2(current + 2, adapters, end, memo)
        + _part2(current + 3, adapters, end, memo)
    )

    memo[(current, end)] = c

    return c
