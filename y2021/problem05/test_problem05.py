from y2021.problem05 import *

example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def test_part1_example():
    assert part1(example) == 5


def test_part2_example():
    assert part2(example) == 12


def test_points_in_line():
    points = list(points_in_line((8, 0), (0, 8), True))
    assert points == [
        (8, 0),
        (7, 1),
        (6, 2),
        (5, 3),
        (4, 4),
        (3, 5),
        (2, 6),
        (1, 7),
        (0, 8),
    ]
