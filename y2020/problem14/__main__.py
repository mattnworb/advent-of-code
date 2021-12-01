from . import *

if __name__ == "__main__":
    with open("y2020/problem14/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", computer(inp))

    print("part 2:", computer(inp, version=2))
