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


def test_part1_example():
    assert part1(example_inp) == 5
