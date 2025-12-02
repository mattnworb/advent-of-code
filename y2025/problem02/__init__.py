from typing import *
from functools import lru_cache


def part1(inp: str):
    sum = 0
    for id_range in inp.split(","):
        start, end = map(int, id_range.split("-"))

        # you can find the invalid IDs by looking for any ID which is made only
        # of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64
        # twice), and 123123 (123 twice) would all be invalid IDs.

        for id in range(start, end + 1):
            id_str = str(id)
            if len(id_str) % 2 != 0:
                continue
            half_point = len(id_str) // 2
            invalid = id_str[0:half_point] == id_str[half_point:]
            if invalid:
                sum += id
    return sum


def part2(inp: str):
    # Now, an ID is invalid if it is made only of some sequence of digits
    # repeated at least twice. So, 12341234 (1234 two times), 123123123 (123
    # three times), 1212121212 (12 five times), and 1111111 (1 seven times) are
    # all invalid IDs.

    # brute force will probably be slow?

    invalids = set()
    for id_range in inp.split(","):
        start, end = map(int, id_range.split("-"))

        for num in range(start, end + 1):
            if part2_is_invalid(num) and num not in invalids:
                # print(f"found invalid ID in range {id_range}: {num}")
                invalids.add(num)
    return sum(invalids)


@lru_cache(maxsize=None)
def part2_is_invalid(num: int) -> bool:
    num_str = str(num)
    if len(num_str) == 1:
        return True

    # the length of id_str controls how long the repeating pattern can be:
    #
    # if digits
    # if digits=2, max pattern length of 1
    # if digits=3, max pattern length of 1
    # if digits=4, max pattern length of 1 or 2
    # if digits=5, max pattern length of 1
    # if digits=6, max pattern length of 1 or 2 or 3
    # if digits=7, max pattern length of 1
    # if digits=8, max pattern length of 1 or 2 or 4
    #
    # these are just the divisors of the length of the string

    # if id_str is 2 digits, a pattern that repeats can only be 1 digit long
    # if id_str is 3 digits, a pattern that repeats can only be 1 digit long
    # if id_str is 4 digits, a pattern that repeats can be 1 or 2 digits long
    # if id_str is 5 digits, a pattern that repeats can only be 1 digit long

    for num_digits in divisors(len(num_str)):
        candidate = True
        for i in range(1, len(num_str) // num_digits):
            # first slice is always the same
            start = num_digits * i
            end = start + num_digits
            if num_str[0:num_digits] != num_str[start:end]:
                # the pattern can't be num_digits long
                candidate = False
                break
        # we've checked that each segment is equal to each other
        if candidate:
            return True

    return False


@lru_cache
def divisors(n: int) -> set[int]:
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            # special rule for this problem - don't count len(str(n))
            if i != 1:
                divisors.add(n // i)

    return divisors
