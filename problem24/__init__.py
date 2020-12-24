from typing import *

# The tiles are all hexagonal; they need to be arranged in a hex grid with a
# very specific color pattern. Not in the mood to wait, you offer to help figure
# out the pattern.
#
# The tiles are all white on one side and black on the other. They start with
# the white side facing up. The lobby is large enough to fit whatever pattern
# might need to appear there.
#
# A member of the renovation crew gives you a list of the tiles that need to be
# flipped over (your puzzle input). Each line in the list identifies a single
# tile that needs to be flipped by giving a series of steps starting from a
# reference tile in the very center of the room. (Every line starts from the
# same reference tile.)
#
# Because the tiles are hexagonal, every tile has six neighbors: east,
# southeast, southwest, west, northwest, and northeast. These directions are
# given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is
# identified by a series of these directions with no delimiters; for example,
# esenee identifies the tile you land on if you start at the reference tile and
# then move one tile east, one tile southeast, one tile northeast, and one tile
# east.
#
# Each time a tile is identified, it flips from white to black or from black to
# white. Tiles might be flipped more than once. For example, a line like `esew`
# flips a tile immediately adjacent to the reference tile, and a line like
# `nwwswee` flips the reference tile itself.
#
# ...
#
# Go through the renovation crew's list and determine which tiles they need to
# flip. After all of the instructions have been followed, how many tiles are
# left with the black side up?
#
# --------------------------------------------------------------------------
#
# Idea:
#
# since the 6 directions are east, southeast, southwest, west, northwest, and
# northeast, this means the hexagons are oriented this way:
#
#       __
#    __/  \__
#   /  \__/  \
#   \__/  \__/
#   /  \__/  \
#
#
# I think we can approximate a x,y grid if we treat a move east or west as
# moving 2 positions on the x-axis, like (0, 0) to (2,0), and NE/SW/NW/SW/ as
# moving +/- 1 on both axises. This way, a series of moves like `nwwswee` - nw,
# w, sw, e, e - brings us back to where we started.
#
# Starting at (0, 0), positions after moving nw, w, sw, e, e:
# - (0,  0)
# - (-1, 1)
# - (-3, 1)
# - (-4, 0)
# - (-2, 0)
# - (0, 0)
#
# The grid seems like it is infinite, and everything starts with the white side
# up. The answer to return is the number of black tiles, so we can store the
# state in a set of x,y positions of the black tiles. When a tile is flipped
# from black to white, remove it from the set.

Position = Tuple[int, int]


def part1(inp: str) -> int:
    return len(process_moves(inp))


def process_moves(inp: str) -> Set[Position]:
    black_tiles: Set[Position] = set()

    for line in inp.strip().split("\n"):

        pos = (0, 0)

        for m in parse_line(line):
            pos = move(pos, m)

        # flip tile we landed on
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)
    return black_tiles


moves = {
    "e": (2, 0),
    "w": (-2, 0),
    "ne": (1, -1),
    "se": (1, 1),
    "nw": (-1, -1),
    "sw": (-1, 1),
}


def move(p: Position, m: str) -> Position:
    x0, y0 = p

    assert m in moves, f"unknown move {m}"

    x1, y1 = moves[m]

    return x0 + x1, y0 + y1


def parse_line(line: str) -> Iterator[str]:
    ix = 0
    while ix < len(line):
        ch = line[ix]
        if ch == "w" or ch == "e":
            yield line[ix]
            ix += 1
        elif ch.startswith("n") or ch.startswith("s"):
            yield line[ix : ix + 2]
            ix += 2
        else:
            raise ValueError(f"unrecognized character: {ch}")


def part2(inp: str, rounds: int):
    black_tiles = process_moves(inp)

    for _ in range(rounds):
        new_set = set(black_tiles)  # copy original set

        # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
        for b in black_tiles:
            count = sum(1 if n in black_tiles else 0 for n in adjacent_tiles(b))
            if count == 0 or count > 2:
                new_set.remove(b)

        # we only need to care about the white tiles that are adjacent to at
        # least one black tile
        white_tiles: Set[Position] = set()
        for t in black_tiles:
            for n in adjacent_tiles(t):
                if n not in black_tiles:
                    white_tiles.add(n)

        # "Any white tile with exactly 2 black tiles immediately adjacent to it
        # is flipped to black."
        for w in white_tiles:
            if sum(1 if a in black_tiles else 0 for a in adjacent_tiles(w)) == 2:
                new_set.add(w)

        black_tiles = new_set

    return len(black_tiles)


def adjacent_tiles(p: Position) -> Iterator[Position]:
    # x, y = p
    for m in moves.keys():
        yield move(p, m)
