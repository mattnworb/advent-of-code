from . import *

ex1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
ex2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]


def test_part1_dumb_solution():
    chain = find_chain(ex1)
    assert chain == [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]

    assert distances(chain) == {1: 7, 3: 5}


def test_part1_smarter():
    assert solve_part1(ex1) == 35


def test_part2():
    assert part2(ex1) == 8
    assert part2(ex2) == 19208


def test_part2_dp():
    assert solve_part2_dp(ex1) == 8
    assert solve_part2_dp(ex2) == 19208
