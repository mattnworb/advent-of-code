from problem11 import *

if __name__ == "__main__":
    with open("problem11/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", solve_part1(inp))

    print("part 2:", solve_part2(inp))
