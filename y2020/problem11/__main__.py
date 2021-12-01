from . import *

if __name__ == "__main__":
    with open("y2020/problem11/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", solve_part1(inp))

    print("part 2:", solve_part2(inp))
