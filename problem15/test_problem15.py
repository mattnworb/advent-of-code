from problem15 import *


def test_part1_example():
    max_round = 2020

    assert part1("0,3,6", max_round) == 436
    assert part1("1,3,2", max_round) == 1
    assert part1("2,1,3", max_round) == 10
    assert part1("1,2,3", max_round) == 27
    assert part1("2,3,1", max_round) == 78
