from y2022.problem15 import *

if __name__ == "__main__":
    with open("y2022/problem15/input") as f:
        inp = f.read(-1).strip()

    ans1 = part1(inp)
    print("part 1: ", ans1, end="")
    if ans1 == 6425133:
        print(" (correct)")
    else:
        print(" (WRONG - expected 6425133")

    print("part 2:", part2(inp, search_space=(0, 4000000)))
