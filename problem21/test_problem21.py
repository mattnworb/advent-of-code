from problem21 import *


def test_parse_input():
    inp = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""
    result = parse_input(inp)
    assert len(result) == 4

    assert result == [
        ({"mxmxvkd", "kfcds", "sqjhc", "nhms"}, {"dairy", "fish"}),
        ({"trh", "fvjkl", "sbzzf", "mxmxvkd"}, {"dairy"}),
        ({"sqjhc", "fvjkl"}, {"soy"}),
        ({"sqjhc", "mxmxvkd", "sbzzf"}, {"fish"}),
    ]


def test_part1_example():
    pass
