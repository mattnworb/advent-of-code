from typing import *


def part1():
    pass


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
        "".join([t[-1] for t in tile]),
        # top reversed (if flipped)
        tile[0][::-1],
        # bottom reversed (if flipped)
        tile[-1][::-1],
        # left and right reversed
        left[::-1],
        right[::-1],
    ]
