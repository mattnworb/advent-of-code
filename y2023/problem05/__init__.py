from typing import *
from collections.abc import Sequence

# dict of range to offset. if a seed falls in the range in the dict key, then it
# should be transformed by adding the offset (dict value) to it
MapTable = Dict[Sequence[int], int]


def part1(inp: str):
    lines = inp.split("\n")
    assert lines[0].startswith("seeds: ")

    seeds = [int(s) for s in lines[0][len("seeds: ") :].split()]

    # assume the maps in the input are in order, like A-to-B map, B-to-C map etc
    map_tables: List[MapTable] = []
    cur_table: MapTable = {}

    # TODO: parsing might be less janky if input was split by "\n\n"
    for line in lines[2:]:
        if line.endswith("map:"):
            # new map
            cur_table = {}
            map_tables.append(cur_table)
        elif line != "":
            # parsing the map, line contains 3 numbers:
            # destination range start, source range start, range length
            dst_range_start, src_range_start, range_len = map(int, line.split())

            offset = dst_range_start - src_range_start
            cur_table[range(src_range_start, src_range_start + range_len)] = offset

    seed_to_final_state: Dict[int, int] = {}
    for seed in seeds:
        result = seed
        for table in map_tables:
            # table is a dict with keys that are ranges
            # figure out which dict entry contains a range containing this value (result). only one shold
            # Any source numbers that aren't mapped correspond to the same destination number
            for rg, offset in table.items():
                if result in rg:
                    result += offset
                    break
        seed_to_final_state[seed] = result

    # find the lowest location number that corresponds to any of the initial seeds
    return min(seed_to_final_state.values())


def part2(inp: str):
    pass
