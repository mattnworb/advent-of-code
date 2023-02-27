from typing import *
from collections import defaultdict


def parse(inp: str) -> Tuple[str, Dict[str, str]]:
    lines = inp.split("\n")
    template = lines[0]

    instructions = {}
    for line in lines[2:]:
        left, right = line.split(" -> ")
        instructions[left] = right
    return template, instructions


def run_steps(template: str, instructions: Dict[str, str], rounds=10) -> Dict[str, int]:
    # the naive approach, which works fine for part1 / 10 rounds, is to treat
    # the polymer as a string (or list of chars), build a copy of the string in
    # each round, iterating over each position in the string. around round 20
    # this gets really slow as the string has a length in the hundreds of
    # thousands or more - concatenation and iteration is slow. Also tried a
    # list[str] and inserting in place, which was even slower, probably because
    # python lists are arrays and inserting in the middle means moving elements.
    #
    # another approach:
    # - the polymer doesn't actually need to be a string, order isn't important
    #   ... all we need to know at the end is frequency of each char
    # - store as dict of pair to count
    # - so "NNCB" becomes {"NN": 1, "NC": 1, "CB": 1}
    # - in each round, walk through each instruction
    # - to "insert" a char between a pair of chars, lets say "NN -> C":
    #   - set new_dict["NC"] += dict["NN"]
    #   - set new_dict["CN"] += dict["NN"]
    #   - set new_dict["NN"] = 0
    #
    # but to count how often each letter appears, have to factor in the first
    # and last char of the template so we don't overcount
    #
    # lets say we started with template "NNCB" and after round 1 we have NCNBCHB
    # which is
    # {"NC": 1, "CN": 1, "NB": 1, "BC": 1, "CH": 1, "HB": 1}
    # raw count is:
    # {"N": 3, "C": 4, "B":3, "H":2}
    # real count is
    # {"N": 2, "C": 2, "B":2, "H":1}
    # each element: int divide by 2, add 1 for first char and last char

    polymer: Dict[str, int] = defaultdict(int)

    for i in range(len(template) - 1):
        polymer[template[i : i + 2]] += 1

    for n in range(rounds):
        # print("starting round", n)
        new_polymer = defaultdict(int, polymer)
        for pair, new_char in instructions.items():
            if pair in polymer:
                new_polymer[pair[0] + new_char] += polymer[pair]
                new_polymer[new_char + pair[1]] += polymer[pair]
                new_polymer[pair] -= polymer[pair]
        polymer = new_polymer
    return polymer


# see above for how this works
def count(template: str, polymer: Dict[str, int]) -> Dict[str, int]:
    # count how often each letter is in the pairs
    c: Dict[str, int] = defaultdict(int)
    for pair, count in polymer.items():
        c[pair[0]] += count
        c[pair[1]] += count
    # divide each value by 2
    for k in c:
        c[k] = c[k] // 2
    # adding back 1 for the first and last char of the template, which stay
    # unchanged in the final polymer
    c[template[0]] += 1
    c[template[-1]] += 1
    return c


def run(inp: str, rounds: int) -> int:
    template, pairs = parse(inp)
    polymer = run_steps(template, pairs, rounds=rounds)
    freqs = count(template, polymer)
    # sort keys in ascending order by value
    sf = sorted(freqs, key=lambda k: freqs[k])
    return freqs[sf[-1]] - freqs[sf[0]]


def part1(inp: str):
    return run(inp, 10)


def part2(inp: str):
    return run(inp, 40)
