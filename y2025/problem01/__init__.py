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
    # You remember from the training seminar that "method 0x434C49434B" means
    # you're actually supposed to count the number of times any click causes the
    # dial to point at 0, regardless of whether it happens during a rotation or
    # at the end of one.

    # Be careful: if the dial were pointing at 50, a single rotation like R1000
    # would cause the dial to point at 0 ten times before returning back to 50!
    pos = 50
    zeros = 0

    for line in inp.splitlines():
        direction = line[0]
        assert direction in ("L", "R")

        amount = int(line[1:])

        if direction == "R":
            if pos == 0:
                crosses = amount // 100
            elif amount >= (100 - pos):
                crosses = (amount - (100 - pos)) // 100 + 1
            else:
                crosses = 0
        else:
            if pos == 0:
                crosses = amount // 100
            elif amount >= pos:
                crosses = (amount - pos) // 100 + 1
            else:
                crosses = 0

        zeros += crosses

        if direction == "L":
            newpos = (pos - amount) % 100
        else:
            newpos = (pos + amount) % 100

        # if pos == 0:
        # print(
        #     f"pos {pos:2}, move {line:4} to {newpos:2}. zeros += {crosses} -> {zeros}"
        # )
        pos = newpos
    return zeros
