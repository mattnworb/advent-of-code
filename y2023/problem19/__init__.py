from typing import *
from dataclasses import dataclass

Part = dict[str, int]
Rule = Callable[[Part], Optional[str]]


def create_comp_rule(category: str, less_than_op: bool, val: int, dest: str) -> Rule:
    def f(part: Part) -> Optional[str]:
        assert category in part
        if less_than_op:
            if part[category] < val:
                return dest
            return None
        else:
            if part[category] > val:
                return dest
            return None

    return f


def create_jump_rule(dest: str) -> Rule:
    def f(part: Part) -> Optional[str]:
        return dest

    return f


def build_workflows(workflow_inp: str) -> dict[str, list[Rule]]:
    workflows: dict[str, list[Rule]] = {}

    for line in workflow_inp.split("\n"):
        name = line[: line.find("{")]
        rules: list[Rule] = []
        for rule in line[line.find("{") + 1 : -1].split(","):
            if ":" in rule:
                # condition to eval
                assert rule[1] in (
                    "<",
                    ">",
                ), f"expected > or < but got '{rule[1]}' in rule '{rule}'"
                category = rule[0]
                val = int(rule[2 : rule.find(":")])
                dest = rule[rule.find(":") + 1 :]
                func = create_comp_rule(category, rule[1] == "<", val, dest)
            else:
                dest = rule
                func = create_jump_rule(dest)
            rules.append(func)
        workflows[name] = rules
    return workflows


def part1(inp: str):
    workflow_inp, ratings_inp = inp.split("\n\n")

    workflows = build_workflows(workflow_inp)

    accepted_parts: list[Part] = []

    for line in ratings_inp.split("\n"):
        part: Part = {}
        for s in line[1:-1].split(","):
            sp = s.split("=")
            part[sp[0]] = int(sp[1])

        rule_iter = iter(workflows["in"])
        next_workflow = None
        while next_workflow not in ["A", "R"]:
            next_workflow = next(rule_iter)(part)
            if next_workflow and next_workflow not in ["A", "R"]:
                rule_iter = iter(workflows[next_workflow])

        if next_workflow == "A":
            accepted_parts.append(part)

    return sum(sum(rating for rating in part.values()) for part in accepted_parts)


@dataclass
class EvalRule:
    category: str
    op: str
    val: int
    dest: str

    def negate(self) -> "EvalRule":
        return EvalRule(
            self.category, ">" if self.op == "<" else "<", self.val, self.dest
        )


def negate(condition: str) -> str:
    if "<" in condition:
        return condition.replace("<", ">=")
    elif ">" in condition:
        return condition.replace(">", "<=")
    return condition


def range_intersection(a: range, b: range) -> range:
    assert a.step == b.step == 1
    return range(max(a.start, b.start), min(a.stop, b.stop))


def part2(inp: str):
    # there are 4000^4 == 2.56e14 possible parts if each of the four ratings can
    # have values between 1-4000. so we can't brute force it quickly.
    #
    # so instead, build a graph of which workflows lead to which, with edge
    # labels as the condition (if any). then find the paths that lead to A, and
    # figure out what range of values for each category is allowable
    #
    # example: {"pv": OrderedDict(**{"a<2006": "qkq", "m>2090": "A", "": "rfg"}}
    graph: dict[str, dict[str, str]] = {}

    for line in inp.split("\n\n")[0].split("\n"):
        name = line[: line.find("{")]
        rules: dict[str, str] = OrderedDict()
        for rule in line[line.find("{") + 1 : -1].split(","):
            if ":" in rule:
                # condition to eval
                assert rule[1] in (
                    "<",
                    ">",
                ), f"expected > or < but got '{rule[1]}' in rule '{rule}'"
                category = rule[0]
                val = int(rule[2 : rule.find(":")])
                dest = rule[rule.find(":") + 1 :]
                # TODO a better type for the condition than a string?
                # er = EvalRule(category, rule[1],val, dest)
                rules[rule[: rule.find(":")]] = dest
            else:
                dest = rule
                rules[""] = dest
            graph[name] = rules

    # - find all paths in graph starting at 'in' and ending in 'A', where the
    #   path is a list of conditions like "s<1351,a<2006,x<1416"
    # - for each path, calculate the number of combinations of parts that
    #   satisfy those conditions
    def dfs(v, paths, path):
        if v not in graph:
            return
        prev_edge = None
        for edge, n in graph[v].items():
            if graph[v][edge] == "A":
                paths.append(merge_paths(path, prev_edge, edge))
            elif graph[v][edge] != "R":
                dfs(n, paths, merge_paths(path, prev_edge, edge))
            prev_edge = edge

    def merge_paths(path, prev_edge, edge):
        new_path = list(path)
        if prev_edge:
            new_path.append(negate(prev_edge))
        if edge != "":
            new_path.append(edge)
        return new_path

    paths: list[str] = []
    dfs("in", paths, [])

    print(paths)

    combinations = 0
    for path in paths:
        ranges = {
            "x": range(1, 4001),
            "s": range(1, 4001),
            "a": range(1, 4001),
            "m": range(1, 4001),
        }

        for condition in path:
            cat = condition[0]
            assert cat in ranges
            if ">=" in condition:
                r = range(int(condition[3:]), 4001)
            elif "<=" in condition:
                r = range(1, int(condition[3:]) + 1)
            elif ">" in condition:
                r = range(int(condition[2:]) + 1, 4001)
            elif "<" in condition:
                r = range(1, int(condition[2:]))
            else:
                raise ValueError("bad op")
            ranges[cat] = range_intersection(ranges[cat], r)

        # TODO: this doesn't account for *distinct* combinations
        # paths=[['s<1351', 'a<2006', 'x<1416'],
        #        ['s<1351', 'a<2006', 'x>=1416', 'x>2662'],
        #        ['s<1351', 'a>=2006', 'm>2090'],
        #        ['s<1351', 'm<=2090', 'x<=2440'],
        #        ['s>=1351', 's>2770', 's>3448'],
        #        ['s>=1351', 's>2770', 's<=3448', 'm>1548'],
        #        ['s>=1351', 's>2770', 's<=3448', 'm<=1548'],
        #        ['s>=1351', 's<=2770', 'm<1801', 'm>838'],
        #        ['s>=1351', 's<=2770', 'm<1801', 'm<=838', 'a<=1716']
        #       ]
        combinations += (
            len(ranges["x"]) * len(ranges["s"]) * len(ranges["a"]) * len(ranges["m"])
        )

    return combinations
