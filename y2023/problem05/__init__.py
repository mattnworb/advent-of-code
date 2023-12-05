from typing import *

MapTable = Dict[int, int]


# TODO: this will be too slow with actual input as the range_lengths are in the hundreds of millions
def part1(inp: str):
    lines = inp.split("\n")
    assert lines[0].startswith("seeds: ")

    seeds = [int(s) for s in lines[0][len("seeds: ") :].split()]

    # assume the maps in the input are in order, like A-to-B map, B-to-C map etc
    map_tables: List[MapTable] = []
    cur_table: MapTable = {}

    for line in lines[2:]:
        if line.endswith("map:"):
            # new map
            cur_table = {}
            map_tables.append(cur_table)
        elif line != "":
            # parsing the map, line contains 3 numbers:
            # destination range start, source range start, range length
            dst_range_start, src_range_start, range_len = map(int, line.split())
            for i in range(range_len):
                cur_table[src_range_start + i] = dst_range_start + i

    seed_to_final_state: MapTable = {}
    for seed in seeds:
        result = seed
        for table in map_tables:
            # Any source numbers that aren't mapped correspond to the same destination number
            if result in table:
                result = table[result]
        seed_to_final_state[seed] = result

    # find the lowest location number that corresponds to any of the initial seeds
    return min(seed_to_final_state.values())


def part2(inp: str):
    pass
