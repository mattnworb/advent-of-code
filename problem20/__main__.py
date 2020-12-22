from problem20 import *

if __name__ == "__main__":
    with open("problem20/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", part1(inp))
    print()
    print("part 2:", part2(inp))
