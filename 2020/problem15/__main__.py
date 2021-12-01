from problem15 import *

if __name__ == "__main__":
    # with open("problem15/input") as f:
    #    inp = f.read(-1).strip()

    inp = "16,1,0,18,12,14,19"

    print("part 1:", solve(inp, 2020))

    print("part 2:", solve(inp, 30_000_000))
