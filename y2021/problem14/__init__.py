from typing import *


def parse(inp: str) -> Tuple[str, Dict[str, str]]:
    lines = inp.split("\n")
    template = lines[0]

    instructions = {}
    for line in lines[2:]:
        left, right = line.split(" -> ")
        instructions[left] = right
    return template, instructions


def run_steps(template: str, insertions: Dict[str, str], rounds=10) -> str:
    polymer = template

    for n in range(rounds):
        next_polymer = ""
        for i in range(len(polymer) - 1):
            p = polymer[i : i + 2]
            if p in insertions:
                # don't insert p[1] as next step will get that
                next_polymer += p[0] + insertions[p]
            else:
                next_polymer += p[0]
        # last char
        next_polymer += polymer[-1]
        polymer = next_polymer
    return polymer


def part1(inp: str):
    template, pairs = parse(inp)
    polymer = run_steps(template, pairs, 10)
    c = Counter(polymer)
    freq = c.most_common()
    return freq[0][1] - freq[-1][1]


def part2(inp: str):
    pass
