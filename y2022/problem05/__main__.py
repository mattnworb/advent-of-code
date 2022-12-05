from y2022.problem05 import *

if __name__ == "__main__":
    with open("y2022/problem05/input") as f:
        # don't strip leading whitespace - the leading whitespace is important
        # for this problem
        inp = f.read(-1).rstrip()

    print("part 1:", part1(inp))

    print("part 2:", part2(inp))
