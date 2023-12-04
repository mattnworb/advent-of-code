from typing import *
from collections import Counter


def part1(inp: str):
    part_numbers: Set[int] = set()
    all_numbers: Counter[int] = Counter()

    grid = inp.split("\n")

    def is_symbol(x, y):
        return grid[y][x] != "." and not grid[y][x].isdigit()

    x_range = range(len(grid[0]))
    y_range = range(len(grid))

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
        at_number = False
        current_number = ""
        for x, ch in enumerate(line):
            if (at_number and not ch.isdigit()) or (
                ch.isdigit() and x == (len(line) - 1)
            ):
                # number is done
                part_number = int(current_number)
                all_numbers[part_number] += 1

                x_start = x - len(current_number)
                x_end = x - 1  # we are already one past the end of the number

                # reset
                at_number = False
                current_number = ""

                # check if it touches a symbol
                touches_symbol = False

                # check above and below, including diagonals
                for i in range(max(0, x_start - 1), min(len(grid[y]) - 1, x_end + 2)):
                    if y - 1 in y_range and is_symbol(i, y - 1):
                        touches_symbol = True
                    if y + 1 in y_range and is_symbol(i, y + 1):
                        touches_symbol = True

                # and left and right in this row
                if x_start - 1 in x_range and is_symbol(x_start - 1, y):
                    touches_symbol = True
                if x_end + 1 in x_range and is_symbol(x_end + 1, y):
                    touches_symbol = True

                if touches_symbol:
                    part_numbers.add(part_number)

                print(f"{part_number} at ({x_start}, {y}), touches={touches_symbol}")
                print_surrounding(x_start, x_end, y)
                print()
            elif ch.isdigit():
                at_number = True
                current_number += ch
    # numbers might be repeated in the input but not always touching a symbol
    # the sum should include ALL of them
    # "There are lots of numbers and symbols you don't really understand, but
    # apparently any number adjacent to a symbol, even diagonally, is a "part
    # number" and should be included in your sum."

    return sum(n for n in all_numbers.elements() if n in part_numbers)


def part2(inp: str):
    pass
