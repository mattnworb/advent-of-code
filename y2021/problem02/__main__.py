from y2021.problem02 import *

if __name__ == "__main__":
    with open("y2021/problem02/input") as f:
        inp = f.read(-1).strip()

    commands = inp.split("\n")

    print("part 1:", part1(commands))

    print("part 2:", part2(commands))
