from typing import *
from collections import Counter
from functools import reduce
from operator import mul

# some thoughts on an approach:
#
# only the borders of each tile matter
#
# since the border of one tile and the border of the tile next to it have to be
# equal, we can count how often each border (which is just a string) occurs in
# the total set of tiles.
#
# any border that only occurs once must be on the edge of the original image
# with everything put together
#
# if a tile has two borders that only occur once - is that a corner piece? No,
# because the tile could be flipped (horizontally or vertically), which means
# some "borders" are never actually used / matched up with other tiles.
#
# But from inspecting the data, there are only four tiles that have 3 unique
# borders - which seems like those must be the corner pieces.
def part1(inp: str) -> int:
    tiles = parse_input(inp)

    # dict of border (string) to count (int)
    border_counts = Counter(b for t in tiles.values() for b in borders(t))

    corner_tile_nums: Set[int] = set()

    for tile_num, tile in tiles.items():
        # count how many times each border appears once
        c = sum(1 for b in borders(tile) if border_counts[b] == 1)
        # print(f"tile {tile_num} has unique borders: {c}")
        if c >= 3:
            print(f"found corner tile: {tile_num}")
            corner_tile_nums.add(tile_num)

    assert len(corner_tile_nums) == 4

    return reduce(mul, corner_tile_nums)


Tile = List[str]


def parse_input(inp: str) -> Dict[int, Tile]:
    tiles: Dict[int, Tile] = {}
    for section in inp.strip().split("\n\n"):
        lines = section.split("\n")
        # first line should be like "Tile <num>:"
        assert lines[0].startswith("Tile ")
        num = lines[0].split(" ")[1].replace(":", "")
        tiles[int(num)] = lines[1:]
    return tiles


def borders(tile: Tile) -> List[str]:
    left = "".join([t[0] for t in tile])
    right = "".join([t[-1] for t in tile])

    return [
        # top
        tile[0],
        # bottom
        tile[-1],
        # left side
        left,
        # right side
        right,
        # top reversed (if flipped)
        tile[0][::-1],
        # bottom reversed (if flipped)
        tile[-1][::-1],
        # left and right reversed
        left[::-1],
        right[::-1],
    ]
