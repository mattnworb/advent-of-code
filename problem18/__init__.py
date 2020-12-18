from typing import *


# Instructions:
#
# The homework (your puzzle input) consists of a series of expressions that
# consist of addition (+), multiplication (*), and parentheses ((...)). Just
# like normal math, parentheses indicate that the expression inside must be
# evaluated before it can be used by the surrounding expression. Addition still
# finds the sum of the numbers on both sides of the operator, and multiplication
# still finds the product.
#
# However, the rules of operator precedence have changed. Rather than evaluating
# multiplication before addition, the operators have the same precedence, and
# are evaluated left-to-right regardless of the order in which they appear.


# so this is basically an exercise in converting an expression into polish / reverse polish notation

Operand = int
Operator = str
Either = Union[Operand, Operator]


def tokenize(line: str) -> List[str]:
    return [c for c in line if not c.isspace()]


# NOTE: the problem input only contains addition and multiplication, so those are left out here
def is_left_associative(token: Operator) -> bool:
    return token in ["+", "*"]


def precedence(token: Operator, part1: bool) -> int:
    assert token in ["+", "*"]
    if part1:
        return 1
    if token == "+":
        return 2
    # if token == "*":
    return 1


def parse_expression(line: str, part1=True) -> List[Either]:
    output: List[Either] = []
    operators: List[Operator] = []

    for token in tokenize(line):
        if token.isnumeric():
            output.append(int(token))

        # check if operator
        elif token not in ["(", ")"]:

            while (
                len(operators) > 0
                # normally this would also check if operator at the top of the
                # stack has greater precedence than the token:
                # "and ((the operator at the top of the operator stack has
                # greater precedence) or (the operator at the top of the
                # operator stack has equal precedence and the token is left
                # associative))"
                # ... but everything here has equal precedence
                and operators[0] not in ["(", ")"]
                and (
                    precedence(operators[0], part1) > precedence(token, part1)
                    or (
                        precedence(operators[0], part1) == precedence(token, part1)
                        and is_left_associative(token)
                    )
                )
                and operators[0] != "("
            ):
                output.append(operators.pop(0))
            operators.insert(0, token)

        elif token == "(":
            operators.insert(0, token)

        elif token == ")":
            while operators[0] != "(":
                output.append(operators.pop(0))
            if operators[0] == "(":
                operators.pop(0)  # discard

    while len(operators) > 0:
        output.append(operators.pop(0))

    return output


def evaluate(expression: List[Either]) -> int:
    stack: List[Operand] = []

    for op in expression:
        if isinstance(op, Operand):
            stack.insert(0, op)
        elif isinstance(op, Operator):
            a = stack.pop(0)
            b = stack.pop(0)

            if op == "+":
                result = a + b
            elif op == "*":
                result = a * b
            else:
                raise ValueError(f"unknown operator: {op}")

            stack.insert(0, result)
        else:
            raise ValueError(f"unknown type {op}")

    assert len(stack) == 1

    return stack[0]


# Evaluate the expression on each line of the homework; what is the sum of the
# resulting values?
def part1(inp: str) -> int:
    return sum(evaluate(parse_expression(line)) for line in inp.strip().split("\n"))


def part2(inp: str) -> int:
    return sum(
        evaluate(parse_expression(line, part1=False))
        for line in inp.strip().split("\n")
    )
