from typing import *


def parse(inp: str) -> Tuple[str, Dict[str, str]]:
    lines = inp.split("\n")
    template = lines[0]

    instructions = {}
    for line in lines[2:]:
        left, right = line.split(" -> ")
        instructions[left] = right
    return template, instructions


def run_steps(template: str, insertions: Dict[str, str], rounds=10) -> List[str]:
    polymer = list(template)

    for n in range(rounds):
        print("starting round", n)
        next_polymer = []
        for i in range(len(polymer) - 1):
            p = polymer[i : i + 2]
            next_polymer.append(p[0])
            pstr = p[0] + p[1]
            if pstr in insertions:
                next_polymer.append(insertions[pstr])
            # don't insert p[1] here as next step will get that
        # last char
        next_polymer.append(polymer[-1])
        polymer = next_polymer
    return polymer


def part1(inp: str):
    template, pairs = parse(inp)
    polymer = run_steps(template, pairs, rounds=10)
    c = Counter(polymer)
    freq = c.most_common()
    return freq[0][1] - freq[-1][1]


def part2(inp: str):
    template, pairs = parse(inp)
    polymer = run_steps(template, pairs, rounds=40)
    c = Counter(polymer)
    freq = c.most_common()
    return freq[0][1] - freq[-1][1]
