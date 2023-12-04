from typing import *

# from collections import Counter
import re


def part1(inp: str):
    grid = inp.split("\n")

    def is_symbol(x, y):
        return grid[y][x] != "." and not grid[y][x].isdigit()

    x_range = range(len(grid[0]))
    y_range = range(len(grid))
    part_numbers: List[int] = []

    def print_surrounding(x_start, x_end, y):
        for py in range(y - 1, y + 2):
            if py not in y_range:
                continue
            for px in range(x_start - 1, x_end + 2):
                if px not in x_range:
                    continue
                print(grid[py][px], end="")
            print()

    for y, line in enumerate(grid):
        for m in re.finditer(r"(\d+)", line):
            # x_start is index where the number begins, x_end is one past the last digit
            x_start, x_end = m.span()
            part_number = int(m.group())

            # check if it touches a symbol
            touches_symbol = False

            # check above and below, including diagonals
            # for i in range(max(0, x_start - 1), min(len(grid[y]) - 1, x_end + 1)):
            for i in range(x_start - 1, x_end + 1):
                if i not in x_range:
                    continue
                if y - 1 in y_range and is_symbol(i, y - 1):
                    touches_symbol = True
                if y + 1 in y_range and is_symbol(i, y + 1):
                    touches_symbol = True

            # and left and right in this row
            if x_start - 1 in x_range and is_symbol(x_start - 1, y):
                touches_symbol = True
            if x_end in x_range and is_symbol(x_end, y):
                touches_symbol = True

            if touches_symbol:
                part_numbers.append(part_number)

            # print(f"{part_number} at ({x_start}, {y}), touches={touches_symbol}")
            # print_surrounding(x_start, x_end, y)
            # print()

    return sum(part_numbers)


def part2(inp: str):
    pass
