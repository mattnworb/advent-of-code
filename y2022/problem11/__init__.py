from typing import *
from dataclasses import dataclass
from collections import Counter
from functools import reduce
import operator


@dataclass
class Monkey:
    # num: int
    items: List[int]
    # maybe represent this as a Callable
    op: Callable[[int], int]
    test_divisor: int
    throw_to_if_true: int
    throw_to_if_false: int


def parse(inp: str) -> List[Monkey]:
    monkeys = []
    for section in inp.split("\n\n"):
        lines = section.split("\n")
        # num = int(lines[0][len("Monkey: ") + 1 : -1])
        items = list(map(int, lines[1].split(": ")[1].split(",")))

        # op line is like "  Operation: new = old + 8"
        tokens = lines[2].split(" ")
        operation, operand = tokens[6], tokens[7]
        assert operation in ["+", "*"]

        if operand == "old":
            if operation == "+":
                op = lambda o: o + o
            else:
                op = lambda o: o * o
        else:
            n = int(operand)
            if operation == "+":
                # defining num as a param of the lambda with a default value is
                # to workaround python lambda's not closing over the value of n;
                # the lambda when executed will refer to the last assignment to
                # n. https://stackoverflow.com/a/2295368
                op = lambda o, num=n: o + num  # type:ignore
            else:
                op = lambda o, num=n: o * num  # type:ignore

        phrase = "  Test: divisible by "
        assert phrase in lines[3], "unknown test line: " + lines[3]
        divisor = int(lines[3][len(phrase) :])

        phrase = "    If true: throw to monkey "
        assert phrase in lines[4]
        if_true = int(lines[4][len(phrase) :])

        phrase = "    If false: throw to monkey "
        assert phrase in lines[5]
        if_false = int(lines[5][len(phrase) :])

        monkeys.append(Monkey(items, op, divisor, if_true, if_false))

    return monkeys


def do_business(
    monkeys: List[Monkey], num_rounds: int, worry_func: Callable[[int], int]
) -> int:
    inspections: Counter[int] = Counter()

    for round in range(num_rounds):
        # print("starting round", round)
        for monkey_num, monkey in enumerate(monkeys):
            # print("at monkey", monkey_num)
            if monkey.items:
                # inspect each item the monkey has
                for itemix, worry in enumerate(monkey.items):
                    inspections[monkey_num] += 1

                    worry = monkey.op(worry)
                    worry = worry_func(worry)

                    monkey.items[itemix] = worry

                    throw_to = (
                        monkey.throw_to_if_true
                        if worry % monkey.test_divisor == 0
                        else monkey.throw_to_if_false
                    )
                    monkeys[throw_to].items.append(worry)

                # clear this monkeys list
                monkey.items = []

    m1, m2 = inspections.most_common(2)
    return m1[1] * m2[1]


def part1(inp: str):
    monkeys = parse(inp)
    return do_business(monkeys, 20, worry_func=lambda w: w // 3)


def part2(inp: str):
    monkeys = parse(inp)

    # the insight here is that if we kept multiplying the worry levels for 10000
    # rounds, the numbers would get gigantic, especially "new = old * old". We
    # want to mutate the worry level to something "managable" but without
    # affecting the results of the division in the "test" step - so we can take
    # the multiple of all the divisors. We know they are all prime from looking
    # at input; if they weren't this could probably be Least Common Multiple
    # (but a larger-than-necessary multiple seems like it would work fine too)
    mult = reduce(operator.mul, (m.test_divisor for m in monkeys))

    return do_business(monkeys, 10000, worry_func=lambda w: w % mult)
