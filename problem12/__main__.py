from problem12 import *

if __name__ == "__main__":
    with open("problem12/input") as f:
        inp = f.read(-1).strip()

    p = make_moves(inp.split("\n"))
    print("part 1:", manhattan_distance(p))

    print("part 2:", "TODO")
