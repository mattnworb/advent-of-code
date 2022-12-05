from y2022.problem05 import *

example = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_part1_example():
    assert part1(example) == "CMZ"


def test_part2_example():
    # TODO: populate
    assert part2(example)
