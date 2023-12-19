from y2023.problem15 import *

example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def test_part1_example():
    assert part1(example) == 1320


def test_part2_example():
    assert part2(example) == 145
