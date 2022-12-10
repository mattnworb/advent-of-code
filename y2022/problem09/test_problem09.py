from y2022.problem09 import *

example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def test_part1_example():
    assert part1(example) == 13


example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def test_part2_example():
    assert part2(example2) == 36
