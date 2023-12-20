from typing import *

Grid = list[list[str]]


def tilt_north(grid: Grid) -> None:
    # mutate in-place

    # scan down the rows of each column
    for c in range(len(grid[0])):
        empties: list[int] = []
        for r in range(len(grid[c])):
            if grid[r][c] == "O" and empties:
                # swap
                first_empty = empties.pop(0)
                grid[first_empty][c] = "O"
                grid[r][c] = "."
                empties.append(r)
            elif grid[r][c] == ".":
                empties.append(r)
            elif grid[r][c] == "#":
                empties.clear()


# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....


def tilt_west(grid: Grid) -> None:
    # scan left-to-right in each row
    for r in range(len(grid)):
        empties: list[int] = []
        for c in range(len(grid[r])):
            if grid[r][c] == "O" and empties:
                # swap
                first_empty = empties.pop(0)
                grid[r][first_empty] = "O"
                grid[r][c] = "."
                empties.append(c)
            elif grid[r][c] == ".":
                empties.append(c)
            elif grid[r][c] == "#":
                empties.clear()


def tilt_south(grid: Grid) -> None:
    # scan UP the rows of each column
    for c in range(len(grid[0])):
        empties: list[int] = []
        for r in range(len(grid[c]) - 1, -1, -1):
            if grid[r][c] == "O" and empties:
                # swap
                first_empty = empties.pop(0)
                grid[first_empty][c] = "O"
                grid[r][c] = "."
                empties.append(r)
            elif grid[r][c] == ".":
                empties.append(r)
            elif grid[r][c] == "#":
                empties.clear()


def tilt_east(grid: Grid) -> None:
    # scan right-to-left in each row
    for r in range(len(grid)):
        empties: list[int] = []
        for c in range(len(grid[r]) - 1, -1, -1):
            if grid[r][c] == "O" and empties:
                # swap
                first_empty = empties.pop(0)
                grid[r][first_empty] = "O"
                grid[r][c] = "."
                empties.append(c)
            elif grid[r][c] == ".":
                empties.append(c)
            elif grid[r][c] == "#":
                empties.clear()


def score(grid: Sequence[Sequence[str]]) -> int:
    total = 0
    for r in range(len(grid)):
        rows_from_south = len(grid) - r
        total += sum(
            [rows_from_south for c in range(len(grid[r])) if grid[r][c] == "O"]
        )
    return total


def part1(inp: str):
    grid: Grid = []
    for line in inp.split("\n"):
        grid.append(list(line))

    tilt_north(grid)
    return score(grid)


def one_spin_cycle(grid: Grid) -> None:
    tilt_north(grid)
    tilt_west(grid)
    tilt_south(grid)
    tilt_east(grid)


def part2(inp: str):
    grid: Grid = []
    for line in inp.split("\n"):
        grid.append(list(line))

    # "This process should work if you leave it running long enough, but you're
    # still worried about the north support beams. To make sure they'll survive
    # for a while, you need to calculate the total load on the north support
    # beams after 1000000000 cycles."

    # note: the number of cycles is how many times to move in all four
    # directions, so we really move 4 billion times total
    cycles = 1_000_000_000  # one billion

    # assume we don't want to actually iterate one billion times, and that
    # after some number of spins, we'll be encountering states we've been at already

    GridSnapshot = tuple[tuple[str, ...], ...]

    def snapshot() -> GridSnapshot:
        return tuple(tuple(row) for row in grid)

    past_states = {snapshot(): 0}
    cyclenum_to_snapshot = {0: snapshot()}

    for n in range(1, 1000):
        one_spin_cycle(grid)

        new_state = snapshot()
        if new_state in past_states:
            cycle_length = n - past_states[new_state]
            # this took some trial and error to stumble upon:
            #
            # we've done n iterations so far, and we have (cycles - n) left to do
            # where in the loop will we be after we do (cycles - n) more?

            prev_iteration = past_states[new_state] + ((cycles - n) % cycle_length)
            return score(cyclenum_to_snapshot[prev_iteration])

        past_states[new_state] = n
        cyclenum_to_snapshot[n] = new_state
