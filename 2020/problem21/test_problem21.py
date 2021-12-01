from problem21 import *


def test_parse_input():
    result = parse_input(example_inp)
    assert len(result) == 4

    assert result == [
        ({"mxmxvkd", "kfcds", "sqjhc", "nhms"}, {"dairy", "fish"}),
        ({"trh", "fvjkl", "sbzzf", "mxmxvkd"}, {"dairy"}),
        ({"sqjhc", "fvjkl"}, {"soy"}),
        ({"sqjhc", "mxmxvkd", "sbzzf"}, {"fish"}),
    ]


def test_solve():
    p1, p2 = solve(example_inp)
    assert p1 == 5
    assert p2 == "mxmxvkd,sqjhc,fvjkl"
