from typing import *


def move_rocks_left(grid: List[str]) -> list[str]:
    new_grid = []

    for line in grid:
        prev_cube_ix = 0
        num_round = 0
        num_empty = 0
        new_line = ""
        for ix in range(len(line)):
            if line[ix] == "O":
                num_round += 1
            elif line[ix] == ".":
                num_empty += 1
            elif line[ix] == "#":
                new_line += "O" * num_round + "." * num_empty + "#"
                prev_cube_ix = ix
                num_round = 0
                num_empty = 0
        # add whatever is left after last #
        if prev_cube_ix != len(line) - 1:
            new_line += "O" * num_round + "." * num_empty
        new_grid.append(new_line)
    return new_grid


# we've inverted the problem so we are moving things to the left (and
# transposing once before that) so the scoring has to be column based instead of
# row based
def score(grid: list[str]) -> int:
    total = 0
    for line in grid:
        for c, ch in enumerate(line):
            if ch == "O":
                total += len(line) - c
    return total


def transpose(grid: list[str]) -> list[str]:
    columns = []
    for c in range(len(grid[0])):
        columns.append("".join(line[c] for line in grid))
    return columns


def part1(inp: str):
    grid: List[str] = []
    for line in inp.split("\n"):
        grid.append(line)

    # transpose as its easier to work with left to right scanning one row at a
    # time when moving things
    grid = move_rocks_left(transpose(grid))
    return score(grid)


def part2(inp: str):
    # "This process should work if you leave it running long enough, but you're
    # still worried about the north support beams. To make sure they'll survive
    # for a while, you need to calculate the total load on the north support
    # beams after 1000000000 cycles."

    # note: the number of cycles is how many times to move in all four directions, so we really move 4 trillion times total
    cycles = 1_000_000_000  # one trillion

    grid: List[str] = []
    for line in inp.split("\n"):
        grid.append(line)

    # in the problem text, everything moves "roll north, then west, then south,
    # then east"

    grid = transpose(grid)

    # move, then spin
    pass
