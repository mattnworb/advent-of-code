from y2021.problem12 import *

example = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


def test_part1_example():
    assert part1(example) == 10


def test_part2_example():
    assert part2(example) == 36
