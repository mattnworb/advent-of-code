from . import *

if __name__ == "__main__":
    with open("y2020/problem07/input") as f:
        inp = f.read(-1).strip()

    g = parse_rules(inp.strip().split("\n"))

    r = reverse(g)
    s = expand("shiny gold", r)
    print("part 1:", len(s))

    num_bags = count_bags("shiny gold", g)
    print("part 2:", num_bags)
