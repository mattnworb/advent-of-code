from typing import *

# from collections import Counter
import re

Span = Tuple[int, int]
Grid = List[str]
NumberPos = Tuple[Span, int]


def is_symbol(grid: Grid, x: int, y: int) -> bool:
    return grid[y][x] != "." and not grid[y][x].isdigit()


def touches_symbol(grid: Grid, span: Span, y: int) -> bool:
    # x_start is index where the number begins, x_end is one past the last digit
    x_start, x_end = span
    x_range = range(len(grid[0]))
    y_range = range(len(grid))

    # check above and below, including diagonals
    # for i in range(max(0, x_start - 1), min(len(grid[y]) - 1, x_end + 1)):
    for i in range(x_start - 1, x_end + 1):
        if i not in x_range:
            continue
        if y - 1 in y_range and is_symbol(grid, i, y - 1):
            return True
        if y + 1 in y_range and is_symbol(grid, i, y + 1):
            return True

    # and left and right in this row
    if x_start - 1 in x_range and is_symbol(grid, x_start - 1, y):
        return True
    if x_end in x_range and is_symbol(grid, x_end, y):
        return True

    return False


def part1(inp: str):
    grid = inp.split("\n")

    part_numbers: List[int] = []

    for y, line in enumerate(grid):
        for m in re.finditer(r"(\d+)", line):
            part_number = int(m.group())

            if touches_symbol(grid, m.span(), y):
                part_numbers.append(part_number)

    return sum(part_numbers)


def neighbor_positions(grid: Grid, x: int, y: int) -> Iterator[Tuple[int, int]]:
    x_range = range(len(grid[0]))
    y_range = range(len(grid))

    for dx in range(-1, 2):
        px = x + dx
        if px not in x_range:
            continue
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            py = y + dy
            if py not in y_range:
                continue
            yield px, py


def part2(inp: str):
    grid = inp.split("\n")

    # different than part1 - store all spans containing part numbers
    # this could just be storing the ones that touch a gear - but its easier to reuse code from part1
    part_number_spans: Dict[NumberPos, int] = {}

    for y, line in enumerate(grid):
        for m in re.finditer(r"(\d+)", line):
            part_number = int(m.group())
            span = m.span()
            if touches_symbol(grid, span, y):
                part_number_spans[(span, y)] = part_number

    # loop again to find the gears ('*') and track the sum of products of the
    # adjacent part numbers
    total = 0
    for gear_y, line in enumerate(grid):
        for m in re.finditer(r"\*", line):
            gear_x = m.span()[0]

            # do two part numbers touch this gear?
            touching_nums = set()
            for px, py in neighbor_positions(grid, gear_x, gear_y):
                for (span, num_y), part_number in part_number_spans.items():
                    if py == num_y and px in range(span[0], span[1]):
                        # instead of a set we could break out of the loop to
                        # avoid counting the same number twice if it touches
                        # twice
                        touching_nums.add(part_number)
                        break

            if len(touching_nums) == 2:
                # could use reduce
                si = iter(touching_nums)
                total += next(si) * next(si)

    return total
