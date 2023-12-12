from typing import *
import itertools

# """Given a record with some question marks, return all possible arrangements that satisfy the constraint"""


Record = Tuple[str, List[int]]


def is_valid(s: str, constraint: List[int]) -> bool:
    sp = s.split(".")
    # split will contain empty strings where 1 or more "." are:
    # In [112]: list(map(len,".###....#.#..#".split("."))#
    # Out[112]: [0, 3, 0, 0, 0, 1, 1, 0, 1]
    return list(filter(lambda n: n > 0, map(len, sp))) == constraint


def all_possible(s: str) -> Iterator[str]:
    """Given a record like '?##?.#', generate all possible outputs, without applying the constraints"""
    num_wildcards = s.count("?")

    # product will yield tuples like ('.', '#', '#', '.', '#')
    for t in itertools.product("#.", repeat=num_wildcards):
        # walk through input string replacing each ? with the next element in t
        new_s = ""
        t_iter = iter(t)
        for ch in s:
            if ch == "?":
                new_s += next(t_iter)
            else:
                new_s += ch
        yield new_s


def part1(inp: str):
    records: List[Record] = []

    for line in inp.split("\n"):
        first, nums = line.split(" ")
        record = (first, list(map(int, nums.split(","))))
        records.append(record)

    total = 0
    for r in records:
        s, constraint = r
        # print("generating all possible inputs for", s)
        total += len(
            list(
                filter(
                    lambda candidate: is_valid(candidate, constraint), all_possible(s)
                )
            )
        )

    return total


def part2(inp: str):
    pass
