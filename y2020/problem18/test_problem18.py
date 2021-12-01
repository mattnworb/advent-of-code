from . import *


def test_tokenize():
    assert tokenize("3 + 4 * (2 - 1)") == ["3", "+", "4", "*", "(", "2", "-", "1", ")"]


def test_parse_expression():
    assert parse_expression("3 + 4") == [3, 4, "+"]

    # assert parse_expression("3 + 4 * (2 - 1)") == [3, 4, "+", 2, 1, "-", "*"]

    # assert parse_expression("(3 + 5) * (7 - 2)") == [3, 5, "+", 7, 2, "-", "*"]

    assert parse_expression("1 + 2 * 3") == [1, 2, "+", 3, "*"]

    assert parse_expression("1 + (2 * 3) + (4 * (5 + 6))") == [
        1,
        2,
        3,
        "*",
        "+",
        4,
        5,
        6,
        "+",
        "*",
        "+",
    ]

    assert parse_expression("1 + 2 * 3 + 4 * 5 + 6") == [
        1,
        2,
        "+",
        3,
        "*",
        4,
        "+",
        5,
        "*",
        6,
        "+",
    ]


def test_part1_example():
    assert evaluate(parse_expression("1 + (2 * 3) + (4 * (5 + 6))")) == 51
    assert evaluate(parse_expression("1 + 2 * 3 + 4 * 5 + 6")) == 71


def test_part2_example():
    assert evaluate(parse_expression("1 + 2 * 3 + 4 * 5 + 6", part1=False)) == 231
