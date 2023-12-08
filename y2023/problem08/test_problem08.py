from y2023.problem08 import *

example1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

example2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def test_part1_example():
    assert part1(example1) == 2
    assert part1(example2) == 6


def test_part2_example():
    # TODO: populate
    assert part2(example1)
