from . import *

if __name__ == "__main__":
    with open("y2020/problem04/input") as f:
        inp = f.read(-1).strip()

    passports = parse_passports(inp)
    valid1 = [is_valid(p) for p in passports]

    print("part 1:", valid1.count(True))

    valid2 = [is_valid(p, check_fields_valid=True) for p in passports]
    print("part 2:", valid2.count(True))
