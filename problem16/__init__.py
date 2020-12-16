from typing import *
from functools import reduce
import operator

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


Rule = List[Sequence[int]]  # is there a type for Range?
Rules = Dict[str, Rule]
Ticket = List[int]


def part1(inp: str) -> int:
    rules, _, nearby_tickets = parse_input(inp)

    invalid_values = []

    for ticket in nearby_tickets:
        for field in ticket:
            # is this field valid for any rule?
            if not any(is_field_valid(rule, field) for rule in rules.values()):
                # if not any(field in r for ranges in rules.values() for r in ranges):
                invalid_values.append(field)

    return sum(invalid_values)


def is_field_valid(rule: Rule, field: int) -> bool:
    return any(field in r for r in rule)


def is_ticket_valid(rule: Rule, ticket: Ticket) -> bool:
    return all(is_field_valid(rule, field) for field in ticket)


def is_ticket_valid_for_all(rules: Rules, ticket: Ticket) -> bool:
    return all(is_ticket_valid(rule, ticket) for rule in rules.values())


def part2(inp: str) -> int:
    rules, my_ticket, nearby_tickets = parse_input(inp)

    def v(ticket):
        for field in ticket:
            if not any(field in r for ranges in rules.values() for r in ranges):
                return False
        return True

    # # TODO: is this needed?
    # nearby_tickets = [t for t in nearby_tickets if is_ticket_valid_for_all(rules, t)]
    nearby_tickets = list(filter(v, nearby_tickets))

    assert len(nearby_tickets) > 0

    order = determine_rule_order(rules, [my_ticket, *nearby_tickets])

    p = []
    for name in rules.keys():
        if name.startswith("departure"):
            p.append(order[name])

    return reduce(operator.mul, p)


# example:
#
#     class: 0-1 or 4-19
#     row: 0-5 or 8-19
#     seat: 0-13 or 16-19
#
#     your ticket:
#     11,12,13
#
#     nearby tickets:
#     3,9,18
#     15,1,5
#     5,14,9
#
# algorithm idea:
#
# 1. create a list of length len(rules) aka len(fields) where each element is a
#    set initially containing all of the rule names.
#
#    candidates = [
#        {"class", "row", "seat"},
#        {"class", "row", "seat"},
#        {"class", "row", "seat"},
#    ]
#
# 2. loop through each ticket, mine and nearby.
# 3. for each field, look at the set of rule names in that position. for each
#    rule name in that set, test if the field value is valid for that rule. If
#    it is not, remove that rule name from the set in that position.
# 4. At the end, there should just be one rule name remaining in each set (I
#    think?)
#
# my ticket: each field is valid for every rule.
#
# nearby ticket [3,9,18]:
# 3 is not valid for class, remove "class" from candidates[0]
# 9 is valid for all
# 18 is valid for all
#
# [15,1,5]:
# 15 is not valid for seat, remove "seat" candidates[0], only "row" is remaining
# 1 is valid for all
# 5 is valid for all
#
# [5,14,9]:
# 5 is valid for "row" (only candidate left in that position)
# 14 is not valid for "seat", remove it from candidates[1]
# 9 is valid for all
#
# result:
# candidates [{"row"}, {"class", "row"}, {"class", "row", "seat"}]
#
# modify algorithm slightly:
#
# 3b. if after removing a candidate from the set in the position, if
#     len(candidates[i]) == 1, remove that rule_name from all other position's
#     sets too
#
# history above plays out the same until:
#
# [15,1,5]:
# 15 is not valid for seat, remove "seat" candidates[0], only "row" is remaining. remove "row" from other positions
# 1 is valid for all
# 5 is valid for all
#
# [5,14,9]:
# 5 is valid for "row" (only candidate in the position)
# 14 is not valid for "seat", remove it from candidates[0] so that only
# "class" is left. remove class from other positions (candidates[2]).
# 9 is valid for all.
#
# result
# candidates [{"row"}, {"class"}, {"seat"}]


def determine_rule_order(rules: Rules, tickets: List[Ticket]) -> Dict[str, int]:

    # one element in this list for each position
    # note: this only creates one set object which breaks below because removing
    # something from candidates[i] removes it from every position:
    # candidates = [set(rules.keys())] * len(tickets[0])
    candidates = [set(rules.keys()) for _ in range(len(tickets[0]))]

    for ticket in tickets:
        print(f"at ticket: {ticket}")
        for ix, field in enumerate(ticket):
            for rule_name in rules.keys():
                if rule_name in candidates[ix] and not is_field_valid(
                    rules[rule_name], field
                ):
                    # print(
                    #     f"field {ix} value={field} of ticket is not valid for rule {rule_name} ({rules[rule_name]})"
                    # )
                    candidates[ix].remove(rule_name)
                    # print(f"remaining candidates for position={ix}: {candidates[ix]}")
                    if len(candidates[ix]) == 1:

                        # remove the value in candidates[ix] from other positions
                        answer_for_ix = extract_name(candidates[ix])
                        # print(
                        #     f"position {ix} must be {answer_for_ix}, removing from other positions"
                        # )
                        for ix2, c in enumerate(candidates):
                            if ix2 != ix and answer_for_ix in c:
                                c.remove(answer_for_ix)

        # print(f"state after processing ticket: {candidates}")

    assert all(
        len(possible_rules) == 1 for possible_rules in candidates
    ), f"did not solve problem after a pass over all tickets, state is {candidates}"

    d = {}
    for ix, possible_rules in enumerate(candidates):

        name = extract_name(possible_rules)
        d[name] = ix + 1  # start at 1
    return d


def extract_name(s: Set[str]) -> str:
    # hack to remove the element from the set, we know it has len == 1
    assert len(s) == 1
    return set(s).pop()


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
