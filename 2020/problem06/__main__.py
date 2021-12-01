from problem06 import *

if __name__ == "__main__":
    with open("problem06/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", count_groups(inp))

    print("part 2:", count_groups(inp, intersect=True))
