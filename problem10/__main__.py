from problem10 import *

if __name__ == "__main__":
    with open("problem10/input") as f:
        inp = f.read(-1).strip()

    adapters = [int(line) for line in inp.split("\n")]

    print("part 1:", solve_part1(adapters))

    print("part 2:", part2(adapters))
