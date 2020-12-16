from typing import *

# example:
# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12

# It doesn't matter which position corresponds to which field; you can identify
# invalid nearby tickets by considering only whether tickets contain values that
# are not valid for any field. In this example, the values on the first nearby
# ticket are all valid for at least one field. This is not true of the other
# three nearby tickets: the values 4, 55, and 12 are are not valid for any
# field. Adding together all of the invalid values produces your ticket scanning
# error rate: 4 + 55 + 12 = 71.
#
# Consider the validity of the nearby tickets you scanned. What is your ticket
# scanning error rate?


def part1(inp: str) -> int:
    rules, _, nearby_tickets = parse_input(inp)

    invalid_values = []

    for ticket in nearby_tickets:
        for field in ticket:
            # is this field valid for any rule?

            if not any(field in r for ranges in rules.values() for r in ranges):
                invalid_values.append(field)

    return sum(invalid_values)


Rule = List[Sequence[int]]  # is there a type for Range?
Rules = Dict[str, Rule]
Ticket = List[int]


def parse_input(inp: str) -> Tuple[Rules, Ticket, List[Ticket]]:
    sections = inp.strip().split("\n\n")
    assert len(sections) == 3

    rules: Rules = {}
    for line in sections[0].strip().split("\n"):
        name, rest = line.split(": ")
        rules[name] = []

        for pair in rest.split(" or "):
            start, end = pair.split("-")
            rules[name].append(range(int(start), int(end) + 1))

    assert sections[1].startswith("your ticket:\n")
    my_t = [int(s) for s in sections[1].split("\n", 2)[1].split(",")]

    assert sections[2].startswith("nearby tickets:\n")
    nearby_t = []
    for line in sections[2].split("\n")[1:]:
        nearby_t.append([int(s) for s in line.split(",")])

    return rules, my_t, nearby_t
