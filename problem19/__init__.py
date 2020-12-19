# They sent you a list of the rules valid messages should obey and a list of
# received messages they've collected so far (your puzzle input).
#
# The rules for valid messages (the top part of your puzzle input) are numbered
# and build upon each other. For example:
#
#   0: 1 2
#   1: "a"
#   2: 1 3 | 3 1
#   3: "b"
#
# Some rules, like 3: "b", simply match a single character (in this case, b).
#
# The remaining rules list the sub-rules that must be followed; for example, the
# rule 0: 1 2 means that to match rule 0, the text being checked must match rule
# 1, and the text after the part that matched rule 1 must then match rule 2.
#
# Some of the rules have multiple lists of sub-rules separated by a pipe (|).
# This means that at least one list of sub-rules must match. (The ones that
# match might be different each time the rule is encountered.) For example, the
# rule 2: 1 3 | 3 1 means that to match rule 2, the text being checked must
# match rule 1 followed by rule 3 or it must match rule 3 followed by rule 1.
#
# Fortunately, there are no loops in the rules, so the list of possible matches
# will be finite. Since rule 1 matches a and rule 3 matches b, rule 2 matches
# either ab or ba. Therefore, rule 0 matches aab or aba.

from typing import *
import re


def part1(inp: str) -> int:
    rules, messages = parse_input(inp)

    assert all(not ch.isnumeric() for ch in rules[0])

    pattern = re.compile(rules[0])

    c = 0
    for line in messages:
        if pattern.fullmatch(line):
            c += 1
    return c
    # return sum(1 if pattern.fullmatch(line) else 0 for line in messages)


def parse_input(inp: str) -> Tuple[Dict[int, str], List[str]]:
    rules_text, messages = inp.strip().split("\n\n")

    raw_rules: Dict[int, str] = {}
    for line in rules_text.split("\n"):
        num, rest = line.split(": ")
        raw_rules[int(num)] = rest

    rules: Dict[int, str] = {}
    for n in raw_rules.keys():
        rules[n] = expand_rules(raw_rules, n)

    return rules, [line.strip() for line in messages.split("\n")]


# TODO memoize?
def expand_rules(raw_rules: Dict[int, str], rule_num: int) -> str:
    if raw_rules[rule_num].startswith('"'):
        return raw_rules[rule_num].replace('"', "")

    output = ""
    for token in raw_rules[rule_num].split(" "):
        # ignore |
        if token.isnumeric():
            output += "(" + expand_rules(raw_rules, int(token)) + ")"
        else:
            output += token
    return output
