from . import *


def test_part1_example():
    max_round = 2020

    assert solve("0,3,6", max_round) == 436
    assert solve("1,3,2", max_round) == 1
    assert solve("2,1,3", max_round) == 10
    assert solve("1,2,3", max_round) == 27
    assert solve("2,3,1", max_round) == 78


def test_part2_example():
    max_round = 30_000_000
    # it takes around 17-20 seconds to run once, so only test a small amount
    assert solve("0,3,6", max_round) == 175594
    assert solve("1,3,2", max_round) == 2578
