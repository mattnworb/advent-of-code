from typing import *


Record = Tuple[str, List[int]]


def count_possible(
    line: str, ix: int, run_length: int, groups: list[int], group_ix: int
) -> int:
    # string = ##..#? 2,1
    # first call: count_possible(line, ix=0, run_length=0, groups, group_ix=0)
    # since line[ix] == #, check if run_length+1 is <= groups[group_ix], since yes,
    #   recurse to count_possible(line, ix=1,run_length=1, groups, group_ix)
    # since line[ix] == #, check if run_length+1 is <= groups[group_ix], since yes,
    #   recurse to count_possible(line, ix=2,run_length=2, groups, group_ix)
    # since line[ix] == ., reset run_length, check if prev char was #, since yes advance group_ix
    #   recurse to count_possible(line, ix=3,run_length=0, groups, group_ix=1)
    # since line[ix] == ., reset run_length, check if prev char was #, since no don't change group_ix
    #   recurse to count_possible(line, ix=4,run_length=0, groups, group_ix=1)
    # since line[ix] == #, check if run_length+1 is <= groups[group_ix], since yes,
    #   recurse to count_possible(line, ix=5,run_length=1, groups, group_ix=1)
    # since line[ix] == ?
    #   check if we can replace it with #
    #     no, since groups[group_ix] == run_length
    #     return 0
    #     (otherwise recurse, passing ix+1 and run_length+1)
    #   replace it with .
    #     increment group_ix since prev char was # (marking transition)
    #     recurse to count_possible(line, ix=6,run_length=0, groups, group_ix=2)
    #
    # base case:
    #   ix >= len(line)
    #   check if group_ix == len(groups) meaning we exhausted them all
    #   return 1 if so else 0

    # don't need both run_length and mutations of group

    if ix >= len(line):
        return 1 if group_ix == len(groups) or run_length == groups[-1] else 0

    if line[ix] == "#":
        # can we go further? answer is no if we've gone over the length of this group
        if run_length + 1 <= groups[group_ix]:
            return count_possible(line, ix + 1, run_length + 1, groups, group_ix)
        else:
            return 0

    if line[ix] == ".":
        # check if we just moved onto a new group
        if ix > 0 and line[ix - 1] == "#":
            return (
                count_possible(line, ix + 1, 0, groups, group_ix + 1)
                if group_ix + 1 < len(groups)
                else 0
            )
        else:
            return count_possible(line, ix + 1, 0, groups, group_ix)

    if line[ix] == "?":
        # pretend we are replacing with "."
        # "did we just move to new group check" again
        # FIXME: this miss the case where line[ix-1] is ?
        if ix > 0 and line[ix - 1] == "#":
            n = (
                count_possible(line, ix + 1, 0, groups, group_ix + 1)
                if group_ix < len(groups)
                else 0
            )
        else:
            n = count_possible(line, ix + 1, 0, groups, group_ix)

        # optionally we can try # too
        if run_length < groups[group_ix]:
            # trying #
            n += count_possible(line, ix + 1, run_length + 1, groups, group_ix)

        return n

    raise ValueError("can't reach here")


def part1(inp: str):
    records: List[Record] = []

    for line in inp.split("\n"):
        first, nums = line.split(" ")
        record = (first, list(map(int, nums.split(","))))
        records.append(record)

    total = 0
    for line, groups in records:
        total += count_possible(line, 0, 0, groups, 0)
    return total


def part2(inp: str):
    pass
