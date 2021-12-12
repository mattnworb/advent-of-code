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
        # discard incomplete lines
        if ch:
            s += scores[ch]
    return s


def complete_line(line: str) -> List[str]:
    open_chars = []
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
                # line is complete - abort
                return []
        else:
            raise ValueError(f"unknown char {ch}")

    # reverse the stack
    solution = []
    while len(open_chars) > 0:
        solution.append(pairs[open_chars.pop()])
    return solution


def part2(inp: str):
    completion_scores = {")": 1, "]": 2, "}": 3, ">": 4}

    scores = []
    for line in inp.split("\n"):
        s = complete_line(line)
        if s:
            # Start with a total score of 0. Then, for each character, multiply
            # the total score by 5 and then increase the total score by the
            # point value given for the character in the following table:
            this_score = 0
            for ch in s:
                this_score *= 5
                this_score += completion_scores[ch]
            scores.append(this_score)
    # Autocomplete tools are an odd bunch: the winner is found by sorting all of
    # the scores and then taking the middle score. (There will always be an odd
    # number of scores to consider.)
    assert len(scores) % 2 == 1, "expected odd number of scores"
    return sorted(scores)[len(scores) // 2]
