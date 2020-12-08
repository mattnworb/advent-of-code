from problem08 import *

if __name__ == "__main__":
    with open("problem08/input") as f:
        inp = f.read(-1).strip()

    code = parse_boot_code(inp)
    c = Console(code)
    normal_exit = c.run_until_done()
    assert normal_exit == False
    print("part 1:", c.accumulator)

    # part2
    acc = solve_halting_problem(code)
    print("part 2:", acc)
