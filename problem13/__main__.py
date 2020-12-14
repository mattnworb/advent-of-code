from problem13 import *

if __name__ == "__main__":
    with open("problem13/input") as f:
        inp = f.read(-1).strip()

    l1, rest = inp.split("\n", 2)
    start_t = int(l1)
    buses = list(int(b) for b in rest.split(",") if b != "x")

    first_t, bus = part1(start_t, buses)
    print("part 1:", first_t * bus, "\n")

    parse_p2_input(inp)
    print("part 2:", part2_find_min_answer(inp))
