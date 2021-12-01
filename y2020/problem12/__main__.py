from . import *

if __name__ == "__main__":
    with open("y2020/problem12/input") as f:
        inp = f.read(-1).strip()

    instructions = inp.split("\n")
    p = part1(instructions)
    print("part 1:", manhattan_distance(p))

    print("part 2:", manhattan_distance(part2(instructions)))
