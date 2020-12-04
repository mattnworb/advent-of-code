from problem04 import *

if __name__ == "__main__":
    with open("problem04/input") as f:
        inp = f.read(-1).strip()

    passports = parse_passports(inp)
    valid = [is_valid(p) for p in passports]

    print("part 1:", valid.count(True))

    print("part 2:", "TODO")
