from . import *

if __name__ == "__main__":
    with open("y2020/problem02/input") as f:
        inp = f.read(-1).strip()

    lines = inp.split("\n")

    print("part 1:", count_valid_passwords_v1(lines))
    print("part 2:", count_valid_passwords_v2(lines))
