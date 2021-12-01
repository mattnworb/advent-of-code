from . import *

if __name__ == "__main__":
    with open("y2020/problem25/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", part1(inp))
