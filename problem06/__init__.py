from typing import List, Set


def count_groups(inp: str) -> int:

    groups = inp.split("\n\n")

    all_answers: List[Set[str]] = []

    for group in groups:
        s: Set[str] = set()

        for line in group.split("\n"):
            s = s.union(set(line))
        all_answers.append(s)

    return sum(len(s) for s in all_answers)
