from . import *

if __name__ == "__main__":
    with open("y2020/problem10/input") as f:
        inp = f.read(-1).strip()

    adapters = [int(line) for line in inp.split("\n")]

    print("part 1:", solve_part1(adapters))

    print("part 2:", solve_part2_dp(adapters))
