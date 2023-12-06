from typing import *
from collections.abc import Sequence

# dict of range to offset. if a seed falls in the range in the dict key, then it
# should be transformed by adding the offset (dict value) to it
MapTable = Dict[range, int]


def parse_map_lines(lines: List[str]) -> List[Tuple[str, MapTable]]:
    # assume the maps in the input are in order, like A-to-B map, B-to-C map etc
    map_tables: List[Tuple[str, MapTable]] = []
    cur_table: MapTable = {}

    for line in lines[2:]:
        if line.endswith("map:"):
            # new map
            cur_table = {}
            map_tables.append((line[: line.find(":")], cur_table))
        elif line != "":
            # parsing the map, line contains 3 numbers:
            # destination range start, source range start, range length
            dst_range_start, src_range_start, range_len = map(int, line.split())

            offset = dst_range_start - src_range_start
            cur_table[range(src_range_start, src_range_start + range_len)] = offset

    return map_tables


def part1(inp: str):
    lines = inp.split("\n")
    assert lines[0].startswith("seeds: ")

    seeds = [int(s) for s in lines[0][len("seeds: ") :].split()]

    map_tables = parse_map_lines(lines)

    seed_to_final_state: Dict[int, int] = {}
    for seed in seeds:
        result = seed
        for table_name, table in map_tables:
            # table is a dict with keys that are ranges. figure out which dict
            # entry contains a range containing this value (result). only one
            # should.
            for rg, offset in table.items():
                if result in rg:
                    result += offset
                    break
                # "Any source numbers that aren't mapped correspond to the same
                # destination number" - no mutation needed here
        seed_to_final_state[seed] = result

    # find the lowest location number that corresponds to any of the initial seeds
    return min(seed_to_final_state.values())


# What is different from part 1 for part 2: when considering the range of seeds,
# we can't add every value between the start and end to the table, because there
# will be millions. so we treat them like ranges the same as we did in part1 for
# the translation tables


def add(r: range, a: int) -> range:
    return range(r.start + a, r.stop + a)


def breakup(src: range, other: range) -> List[range]:
    assert src.step == other.step == 1
    assert src.start < src.stop and src.start < src.stop

    # case where no overlap:
    if src.stop <= other.start or other.stop <= src.start:
        return [src]

    # return 3 items
    # src:    xxxxxx
    # other:    xxx
    #
    # return two items
    # src:    xxxx    or   src:    xxxx
    # other:    xxx        other: xx
    #
    # return one item
    # src:    xxx
    # other: xxxxxx

    result: List[range] = []

    if src.start < other.start:
        result.append(range(src.start, other.start))
    result.append(range(max(src.start, other.start), min(src.stop, other.stop)))
    if src.stop > other.stop:
        result.append(range(other.stop, src.stop))

    return result


def part2(inp: str):
    lines = inp.split("\n")
    assert lines[0].startswith("seeds: ")

    s = lines[0][len("seeds: ") :].split()
    seed_ranges: List[range] = []
    # read two numbers at a time
    for i in range(0, len(s), 2):
        start = int(s[i])
        stop = start + int(s[i + 1])
        seed_ranges.append(range(start, stop))

    map_tables = parse_map_lines(lines)

    mutated_seed_ranges = seed_ranges

    for table_name, table in map_tables:
        # we split the input to this table (seeds, soil, etc) into two lists:
        # one for seeds that have been changed thus far in processing this table
        # (row-by-row), and another for seeds not yet mutated. the latter is
        # what we loop over for each row. once seeds have been mutated by a row,
        # they should not be examined by other rows - promoted to next
        # table/material essentially.
        mutated_to_next_state: List[range] = []
        seed_queue = list(mutated_seed_ranges)

        # for each row in the table, mutate all possible seed ranges, possibly
        # breaking them up into more (but smaller) ranges
        for rg, offset in table.items():
            not_yet_mutated: List[range] = []
            for seed_range in seed_queue:
                if seed_range.stop < rg.start or rg.stop < seed_range.start:
                    # no overlap, so no change
                    not_yet_mutated.append(seed_range)
                    continue

                if seed_range.start < rg.start:
                    # no change to the part that does not overlap
                    not_yet_mutated.append(range(seed_range.start, rg.start))

                # overlapping part, if any
                # or is it always an overlap because of above check?
                overlap = range(
                    max(seed_range.start, rg.start), min(seed_range.stop, rg.stop)
                )
                mutated_to_next_state.append(add(overlap, offset))

                if seed_range.stop > rg.stop:
                    not_yet_mutated.append(range(rg.stop, seed_range.stop))

            # prepare for next row
            seed_queue = not_yet_mutated

        # anything not mutated by this table/round keeps the same value
        mutated_to_next_state.extend(seed_queue)
        mutated_seed_ranges = mutated_to_next_state

    # find the lowest location number that corresponds to any of the initial seeds
    lowest_range = min(mutated_seed_ranges, key=lambda r: r.start)
    return lowest_range.start
