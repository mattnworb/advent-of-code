from typing import List, Dict, Tuple, Set
import re
from collections import defaultdict

Graph = Dict[str, Set[Tuple[int, str]]]


def extract_color(bagname: str) -> str:
    m = re.fullmatch(r"([\w ]+) bags?", bagname)
    if m:
        return m.group(1)
    raise ValueError(f"no match for {bagname}?")


# TODO: this is all a mess, consolidate to one function


def parse_rules(rules: List[str]) -> Graph:
    links: Graph = {}

    for rule in rules:
        left, right = rule.split(" contain ")
        leftbag = extract_color(left)

        s = set()
        if right != "no other bags.":
            for rbag in right.split(", "):
                m = re.fullmatch(r"(\d+) ([\w ]+)s?\.?", rbag)
                if not m:
                    raise ValueError(f"no match for {rbag}?")
                count, bagname = int(m.group(1)), m.group(2)
                s.add((count, extract_color(bagname)))

        if left in links:
            raise ValueError(f"{left} already has a link")

        links[leftbag] = s

    return links


def reverse(g: Graph) -> Dict[str, Set[str]]:
    n: Dict[str, Set[str]] = defaultdict(set)
    for bagname, conns in g.items():
        for count, name in conns:
            n[name].add(bagname)
    return n


def expand(bagname: str, rgraph: Dict[str, Set[str]]) -> Set[str]:
    answer = set()

    queue = set(rgraph[bagname])
    while len(queue) > 0:
        item = queue.pop()
        answer.add(item)
        for b in rgraph[item]:
            queue.add(b)
    return answer


def count_bags(outer_bag: str, g: Graph) -> int:
    n = 0
    for count, inner_bag in g[outer_bag]:
        n += count * (1 + count_bags(inner_bag, g))
    return n
