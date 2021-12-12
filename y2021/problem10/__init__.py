from typing import *

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
openers = pairs.keys()
closers = pairs.values()

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


def find_illegal(line: str) -> Optional[str]:
    open_chars = []  # use as stack
    for ch in line:
        if ch in openers:
            # add to stack
            open_chars.append(ch)

        # is it a valid closer?
        elif ch in closers:
            if len(open_chars) > 0 and ch == pairs[open_chars[-1]]:
                # pop the opener from stack
                open_chars.pop()
            else:
                # illegal closer
                return ch
        else:
            raise ValueError(f"unknown char {ch}")
    return None


def part1(inp: str):
    s = 0
    for line in inp.split("\n"):
        ch = find_illegal(line)
        if ch:
            s += scores[ch]
    return s


def part2(inp: str):
    pass
