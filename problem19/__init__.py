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
    raw_rules, messages = parse_input(inp)

    rules: Dict[int, str] = {}
    for n in raw_rules.keys():
        rules[n] = expand_rules(raw_rules, n)

    # test rule is fully expanded
    assert all(not ch.isnumeric() for ch in rules[0])

    pattern = re.compile(rules[0])
    return sum(1 if pattern.fullmatch(line) else 0 for line in messages)


def part2(inp: str) -> int:
    raw_rules, messages = parse_input(inp)

    raw_rules[8] = "42 | 42 8"
    raw_rules[11] = "42 31 | 42 11 31"

    rules: Dict[int, str] = {}
    for n in raw_rules.keys():
        rules[n] = expand_rules(raw_rules, n)

    pattern = re.compile(rules[0])
    return sum(1 if pattern.fullmatch(line) else 0 for line in messages)


def parse_input(inp: str) -> Tuple[Dict[int, str], List[str]]:
    rules_text, messages = inp.strip().split("\n\n")

    raw_rules: Dict[int, str] = {}
    for line in rules_text.split("\n"):
        num, rest = line.split(": ")
        raw_rules[int(num)] = rest

    return raw_rules, [line.strip() for line in messages.split("\n")]


# TODO memoize?
def expand_rules(raw_rules: Dict[int, str], rule_num: int) -> str:
    rule_text = raw_rules[rule_num]
    if rule_text.startswith('"'):
        return rule_text.replace('"', "")

    # special case for part 2:
    # instead of solving it generically, we have special transformations for these two rules
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    #
    # the loop here can be solved with + in the regex:
    #
    # 8: 42+ (group 42 repeated 1 or more times)
    # 11: 42 repeated N times, 31 repeated N times
    #
    # what are rules 42 and 31?
    # 42: 120 16 | 2 126
    # 31: 2 26 | 120 47

    if rule_num == 8 and rule_text == "42 | 42 8":
        return "(" + expand_rules(raw_rules, 42) + ")+"

    if rule_num == 11 and rule_text == "42 31 | 42 11 31":
        # not sure if it is possible to say "match group 42 N times" and then
        # "match group 31 the same number of times"
        #
        # so lets hack it to say rule 11 is: match 42 31, or match 42 42 31 31,
        # or match 42 42 42 31 31 31, up until 20 times
        #
        # do this by rewriting the rule_text
        #
        # this produces extra spaces but I think it works anyway
        rule_text = " | ".join("42 " * i + "31 " * i for i in range(1, 21))

    output = ""
    for token in rule_text.split(" "):
        # ignore |
        if token.isnumeric():
            output += "(" + expand_rules(raw_rules, int(token)) + ")"
        else:
            output += token
    return output
