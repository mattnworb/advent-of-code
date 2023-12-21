from typing import *


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


def part1(inp: str):
    workflow_inp, ratings_inp = inp.split("\n\n")

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

    # total = 0
    # for part in accepted_parts:
    #     total += sum(rating for rating in part.values())
    # return total

    return sum(sum(rating for rating in part.values()) for part in accepted_parts)


def part2(inp: str):
    return 0
