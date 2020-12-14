from problem14 import *

if __name__ == "__main__":
    with open("problem14/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", computer(inp))

    print("part 2:", computer(inp, version=2))
