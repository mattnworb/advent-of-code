from problem13 import *

if __name__ == "__main__":
    with open("problem13/input") as f:
        inp = f.read(-1).strip()

    l1, rest = inp.split("\n", 2)
    start_t = int(l1)
    buses = parse_buses(rest)

    first_t, bus = part1(start_t, buses)
    print("part 1:", first_t * bus, "\n")

    print("part 2:", part2_sieve(buses))
