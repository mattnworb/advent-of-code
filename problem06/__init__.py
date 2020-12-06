from typing import List, Set

from functools import reduce


def count_groups(inp: str, intersect=False) -> int:

    groups = inp.strip().split("\n\n")

    all_answers: List[Set[str]] = []

    for group in groups:
        s: Set[str] = set()

        # a list of sets
        # answers for each person in the group
        answers = [set(line) for line in group.split("\n")]

        # reduce the list of sets to a single set, using intersection or union
        # depending on the param
        if intersect:
            f = lambda a, b: a.intersection(b)
        else:
            f = lambda a, b: a.union(b)

        reduced = reduce(f, answers)
        all_answers.append(reduced)

    return sum(len(s) for s in all_answers)
