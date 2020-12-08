from problem07 import *

if __name__ == "__main__":
    with open("problem07/input") as f:
        inp = f.read(-1).strip()

    s = expand("shiny gold", parse_rules(inp.strip().split("\n")))
    print("part 1:", len(s))

    print("part 2:", "TODO")
