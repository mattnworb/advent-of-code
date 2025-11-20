from typing import *
import functools

Record = tuple[str, tuple[int, ...]]


@functools.cache
def solve(
    pattern: str,
    ix: int,
    groups: tuple[int, ...],
    group_ix: int,
    run_length: int,
    prev_was_pound: Optional[bool] = None,
) -> int:
    # states to consider
    #
    # each time we are about to use a #, check if it is valid to do so
    # valid: run_length < groups[group_ix]
    # invalid: no more # to consume
    #          run_length >= groups[group_ix]
    #
    # how do we know when we have moved to a new group?
    # arrive at # and not prev_was_pound _and_ there are groups left
    #
    # what to check when arriving at . or about to use one?
    # if prev_was_pound and run_length < groups[group_ix] i.e. did not consume all of active group
    #
    # when are we done?
    # consumed string (ix == len(pattern)), on last group, run_length == groups[group_ix]
    # last part means we pass run_length down always even when using . and only reset when starting new group

    if ix >= len(pattern):
        # line is done
        # this is a valid state if we are on the last group and run_length == last group
        if (group_ix == len(groups) - 1 and run_length == groups[-1]) or (
            # special case for input like ".. 0"
            group_ix == -1 and len(groups) == 1 and groups[0] == 0
        ):
            return 1
        return 0

    def is_pound_valid() -> bool:
        if prev_was_pound:
            return run_length < groups[group_ix]
        # check do we have a new group to start?
        return group_ix < len(groups) - 1

    def is_period_valid() -> bool:
        return not (prev_was_pound and run_length < groups[group_ix])

    if pattern[ix] == "#" and is_pound_valid():
        # did we start a new group of #s?
        if prev_was_pound == False or group_ix == -1:
            # check do we have a new group to start?
            if group_ix == len(groups) - 1:
                return 0
            # new group started
            # do we need to check that the previous one completed all the way?
            return solve(
                pattern, ix + 1, groups, group_ix + 1, run_length=1, prev_was_pound=True
            )
        # continuing previous group, increment run_length
        return solve(
            pattern, ix + 1, groups, group_ix, run_length + 1, prev_was_pound=True
        )

    elif pattern[ix] == "." and is_period_valid():
        return solve(
            pattern, ix + 1, groups, group_ix, run_length, prev_was_pound=False
        )

    elif pattern[ix] == "?":
        # recurse for both . and # - if valid - and add values
        n = 0
        if is_period_valid():
            n += solve(
                pattern,
                ix + 1,
                groups,
                group_ix,
                run_length,
                prev_was_pound=False,
            )

        if is_pound_valid():
            # we can't use a # if this would be starting a new group and we've run out
            # TODO: this condition is wrong when we are on the first group and
            # about to use our first # in the sequence, i.e. "..# 1"
            #
            if prev_was_pound == False or group_ix == -1:
                if group_ix <= len(groups) - 1:
                    # start new group, reset run_length
                    n += solve(
                        pattern,
                        ix + 1,
                        groups,
                        group_ix + 1,
                        run_length=1,
                        prev_was_pound=True,
                    )
            else:
                n += solve(
                    pattern,
                    ix + 1,
                    groups,
                    group_ix,
                    run_length + 1,
                    prev_was_pound=True,
                )
        return n

    # fall through for cases like pattern[ix] == "#" and not is_pound_valid()
    return 0


def part1(inp: str):
    records: List[Record] = []

    for line in inp.split("\n"):
        first, nums = line.split(" ")
        record = (first, tuple(map(int, nums.split(","))))
        records.append(record)

    total = 0
    for line, groups in records:
        total += solve(line, 0, groups, group_ix=-1, run_length=0)
    return total


def part2(inp: str):
    # To unfold the records, on each row, replace the list of spring conditions
    # with five copies of itself (separated by ?) and replace the list of
    # contiguous groups of damaged springs with five copies of itself (separated
    # by ,)
    records: List[Record] = []

    for line in inp.split("\n"):
        first, nums = line.split(" ")
        groups = tuple(map(int, nums.split(","))) * 5
        record = (first + "?" + first + "?" + first + "?" + first + "?" + first, groups)
        records.append(record)

    total = 0
    for line, groups in records:
        total += solve(line, 0, groups, group_ix=-1, run_length=0)
    return total
