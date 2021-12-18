from y2021.problem11 import *

example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def test_adjacent():
    g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert set(adjacent(g, (0, 0))) == {(1, 0), (1, 1), (0, 1)}
    assert set(adjacent(g, (2, 2))) == {(1, 2), (1, 1), (2, 1)}
    assert set(adjacent(g, (1, 2))) == {(0, 2), (2, 2), (0, 1), (1, 1), (2, 1)}


def test_one_round():
    g = parse_input(
        """11111
19991
19191
19991
11111"""
    )
    f = one_round(g)
    assert g == parse_input(
        """34543
40004
50005
40004
34543"""
    )
    assert f == 9


def test_one_round_larger():
    g = parse_input(example)
    one_round(g)
    assert g == parse_input(
        """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""
    )

    one_round(g)
    assert g == parse_input(
        """8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848"""
    )


def test_part1_example():
    assert part1(example) == 1656


def test_part2_example():
    # TODO: populate
    assert part2(example)
