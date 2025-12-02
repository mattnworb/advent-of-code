from typing import *


def part1(inp: str):
    # The dial starts by pointing at 50.
    pos = 50

    # Because the dial is a circle, turning the dial left from 0 one click makes
    # it point at 99. Similarly, turning the dial right from 99 one click makes
    # it point at 0.

    # You could follow the instructions, but your recent required official North
    # Pole secret entrance security training seminar taught you that the safe is
    # actually a decoy. The actual password is the number of times the dial is
    # left pointing at 0 after any rotation in the sequence.
    zeros = 0

    for line in inp.splitlines():
        direction = line[0]
        assert direction in ("L", "R")

        amount = int(line[1:])

        if direction == "L":
            pos = (pos - amount) % 100
        else:
            pos = (pos + amount) % 100

        if pos == 0:
            zeros += 1

    return zeros


def part2(inp: str):
    return 0
