from y2023.problem14 import *

if __name__ == "__main__":
    with open("y2023/problem14/input") as f:
        inp = f.read(-1).strip()

    p1 = part1(inp)
    print("part 1:", p1)
    assert p1 == 108935

    print("part 2:", part2(inp))
