from y2023.problem10 import *

example1 = """
.....
.S-7.
.|.|.
.L-J.
.....
""".strip()

example2 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip()


def test_part1_example():
    assert part1(example1) == 4
    assert part1(example2) == 8


def test_part2_example():
    # TODO: populate
    assert part2(example2)
