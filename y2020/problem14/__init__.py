from typing import *

import re

address_pattern = re.compile(r"\[(\d+)\]")


def computer(program: str, version=1):
    assert version in [1, 2]

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
            v = int(value)

            if version == 1:
                mem[addr] = apply_mask(mask, v)
            elif version == 2:
                for a in apply_mask_v2(mask, addr):
                    mem[a] = v

    # return sum of all non-zero memory values
    return sum(m for m in mem.values())


def apply_mask(mask: str, value: int) -> int:
    # access the chars in the mask in reverse order, so 0 is LSB, etc
    rmask = mask[::-1]
    for i in range(len(mask)):
        ch = rmask[i]
        if ch == "0":
            value = zero_out(value, i)
        elif ch == "1":
            value = one_out(value, i)

    return value


# Values and memory addresses are both 36-bit unsigned integers.
all_ones = (2**36) - 1


def zero_out(x: int, i: int) -> int:
    """Set the i-th bit in the integer x to 0."""
    # XOR the 36-bit all 1s number with a 1 shifted i places left, and
    # then AND x with that to zero out the given bit.
    return x & (all_ones ^ (1 << i))


def one_out(x: int, i: int) -> int:
    """Set the i-th bit in the integer x to 1."""
    # need to simply OR the starting number with a 1 shifted into the right place
    # example, if i ==6:
    # value:  000000000000000000000000000000001011
    # 1 << i: 000000000000000000000000000001000000
    return x | (1 << i)


def apply_mask_v2(mask: str, value: int) -> Set[int]:
    rmask = mask[::-1]

    # this is the same as apply_mask but changed so that 0 bits don't change anything
    for i in range(len(mask)):
        ch = rmask[i]
        # 0 means don't change anything
        if ch == "1":
            value = one_out(value, i)

    addrs = {value}

    for i in range(len(mask)):
        ch = rmask[i]

        if ch == "X":
            copy = set()
            for addr in addrs:
                copy.add(zero_out(addr, i))
                copy.add(one_out(addr, i))
            addrs = copy
    return addrs
