from typing import *

# There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus
# slowly gains energy over time and flashes brightly for a moment when its
# energy is full. Although your lights are off, maybe you could navigate through
# the cave without disturbing the octopuses if you could predict when the
# flashes of light will happen.
#
# The energy level of each octopus is a value between 0 and 9. Here, the
# top-left octopus has an energy level of 5, the bottom-right one has an energy
# level of 6, and so on.
#
# You can model the energy levels and flashes of light in steps. During a single
# step, the following occurs:
#
# - First, the energy level of each octopus increases by 1.
# - Then, any octopus with an energy level greater than 9 flashes. This
#   increases the energy level of all adjacent octopuses by 1, including
#   octopuses that are diagonally adjacent. If this causes an octopus to have an
#   energy level greater than 9, it also flashes. This process continues as long
#   as new octopuses keep having their energy level increased beyond 9. (An
#   octopus can only flash at most once per step.)
# - Finally, any octopus that flashed during this step has its energy level set
#   to 0, as it used all of its energy to flash.
#
# Adjacent flashes can cause an octopus to flash on a step even if it begins
# that step with very little energy.

Grid = List[List[int]]
Pos = Tuple[int, int]


def adjacent(grid: Grid, p: Pos) -> Iterator[Pos]:
    r, c = p
    for r2 in range(r - 1, r + 2):
        for c2 in range(c - 1, c + 2):
            if r2 == r and c2 == c:
                continue
            # check bounds
            if r2 >= 0 and r2 < len(grid) and c2 >= 0 and c2 < len(grid[0]):
                yield r2, c2


def one_round(grid: Grid) -> int:
    """mutate the grid in place, returning number of flashes"""

    flash_queue: Set[Pos] = set()
    # num_flashes = 0  # can remove
    flashed: Set[Pos] = set()

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            # step 1
            grid[r][c] += 1
            if grid[r][c] > 9:
                flash_queue.add((r, c))

    while len(flash_queue) > 0:
        next_to_flash = flash_queue.pop()
        flashed.add(next_to_flash)
        r, c = next_to_flash
        # num_flashes += 1
        # step 2
        for p2 in adjacent(grid, next_to_flash):
            r2, c2 = p2
            grid[r2][c2] += 1
            if grid[r2][c2] > 9 and (r2, c2) not in flashed:
                flash_queue.add((r2, c2))
    # step 3:
    for r, c in flashed:
        grid[r][c] = 0
    return len(flashed)


def parse_input(inp: str) -> Grid:
    return [[int(s) for s in line] for line in inp.split("\n")]


# Given the starting energy levels of the dumbo octopuses in your cavern,
# simulate 100 steps. How many total flashes are there after 100 steps?
def part1(inp: str):
    grid = parse_input(inp)
    flashes = 0
    for _ in range(100):
        f = one_round(grid)
        flashes += f
    return flashes


# If you can calculate the exact moments when the octopuses will all flash
# simultaneously, you should be able to navigate through the cavern. What is the
# first step during which all octopuses flash?
def is_all_zeros(g: Grid) -> bool:
    for row in g:
        if not all(v == 0 for v in row):
            return False
    return True


def part2(inp: str):
    grid = parse_input(inp)
    rounds = 0
    while not is_all_zeros(grid):
        one_round(grid)
        rounds += 1
    return rounds
