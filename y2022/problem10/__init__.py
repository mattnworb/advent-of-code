from typing import *


def part1(inp: str):

    # Start by figuring out the signal being sent by the CPU. The CPU has a
    # single register, X, which starts with the value 1. It supports only two
    # instructions:

    # `addx V` takes two cycles to complete. After two cycles, the X register is
    # increased by the value V. (V can be negative.) `noop`` takes one cycle to
    # complete. It has no other effect.

    # Maybe you can learn something by looking at the value of the X register
    # throughout execution. For now, consider the signal strength (the cycle
    # number multiplied by the value of the X register) during the 20th cycle
    # and every 40 cycles after that (that is, during the 20th, 60th, 100th,
    # 140th, 180th, and 220th cycles).

    # Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and
    # 220th cycles. What is the sum of these six signal strengths?

    instructions = iter(inp.split("\n"))
    strengths = []

    x = 1
    v = 0
    inst = ""
    next_inst_counter = 0

    for cycle in range(1, 221):
        # check if we should load next instruction
        if next_inst_counter == 0:
            inst = next(instructions)
            if inst.startswith("addx"):
                sp = inst.split(" ")
                inst = sp[0]
                v = int(sp[1])

            if inst == "noop":
                next_inst_counter = 1
            elif inst == "addx":
                next_inst_counter = 2

        if cycle == 20 or (cycle - 20) % 40 == 0:
            strengths.append(cycle * x)

        # cycle is done
        next_inst_counter -= 1
        # is the instruction done executing?
        if next_inst_counter == 0:
            if inst == "addx":
                x += v

    return sum(strengths)


def part2(inp: str):
    pass
