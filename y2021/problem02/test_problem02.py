from y2021.problem02 import *


def test_part1_example():
    cmds = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip().split(
        "\n"
    )
    assert part1(cmds) == 150


def test_part2_example():
    cmds = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip().split(
        "\n"
    )
    assert part2(cmds) == 900
