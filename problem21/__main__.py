from problem21 import *


if __name__ == "__main__":
    with open("problem21/input") as f:
        inp = f.read(-1).strip()

    # print("part 1 (example) :", part1(example_inp))

    part1, part2 = solve(inp)

    print("part 1 (my input):", part1)

    print("part 2:", part2)
