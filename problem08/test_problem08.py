from problem08 import *

program = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def test_part1_example():
    c = Console(parse_boot_code(program))
    normal_exit = c.run_until_done()
    assert normal_exit == False
    assert c.accumulator == 5


def test_part2():
    code = parse_boot_code(program)
    assert solve_halting_problem(code) == 8
