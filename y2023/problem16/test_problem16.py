from y2023.problem16 import *

example = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""


def test_part1_example():
    assert part1(example) == 46


def test_part2_example():
    assert part2(example) == 51
