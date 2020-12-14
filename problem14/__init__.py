from typing import *

import re

address_pattern = re.compile(r"\[(\d+)\]")


def part1(program: str):
    mem: Dict[int, int] = {}
    mask = ""

    for line in program.strip().split("\n"):
        instr, value = line.split(" = ")

        if instr == "mask":
            mask = value

        elif instr.startswith("mem["):
            m = address_pattern.search(instr)
            assert m is not None
            addr = int(m.group(1))

            mem[addr] = apply_mask(mask, int(value))

    # return sum of all non-zero memory values
    return sum(m for m in mem.values())


# Values and memory addresses are both 36-bit unsigned integers.
all_ones = (2 ** 36) - 1


def apply_mask(mask: str, value: int) -> int:
    x = value

    # access the chars in the mask in reverse order, so 0 is LSB, etc
    rmask = mask[::-1]
    for i in range(len(mask)):
        ch = rmask[i]
        if ch == "0":
            # zero out the i-th bit.
            # XOR the 32-bit all 1s number with a 1 shifted i places left, and
            # then AND x with that to zero out the given bit.
            x &= all_ones ^ (1 << i)
        elif ch == "1":
            # set the i-th bit to 1.
            # need to simply OR the starting number with a 1 shifted into the right place
            # example, if i ==6:
            # value:  000000000000000000000000000000001011
            # 1 << i: 000000000000000000000000000001000000
            x |= 1 << i

    return x
