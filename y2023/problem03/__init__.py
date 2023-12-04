from typing import *


def part1(inp: str):
    part_numbers: List[int] = []
    grid = inp.split("\n")

    def is_symbol(x, y):
        return grid[y][x] != "." and not grid[y][x].isdigit()

    x_range = range(len(grid[0]))
    y_range = range(len(grid))

    for y, line in enumerate(grid):
        at_number = False
        current_number = ""
        for x, ch in enumerate(line):
            if ch.isdigit():  # and (x, y) not in number_positions:
                at_number = True
                current_number += ch
            elif at_number:
                # number is done
                part_number = int(current_number)
                x_start = x - len(current_number)
                x_end = x - 1

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
                    part_numbers.append(part_number)
                else:
                    print("not touching:", part_number)

    print(part_numbers)
    return sum(part_numbers)


def part2(inp: str):
    pass
