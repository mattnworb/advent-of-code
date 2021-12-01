from problem22 import *


def test_part1_example():
    # from example:
    d1 = [9, 2, 6, 3, 1]
    d2 = [5, 8, 4, 7, 10]

    r1, r2 = play_game(d1, d2)
    assert r1 == []
    assert r2 == [3, 2, 10, 6, 8, 5, 9, 4, 7, 1]


def test_score():
    assert score([3, 2, 10, 6, 8, 5, 9, 4, 7, 1]) == 306


def test_play_game2():
    d1 = [9, 2, 6, 3, 1]
    d2 = [5, 8, 4, 7, 10]

    r1, r2, w = play_game2(d1, d2)
    assert w == 2
    assert r1 == []
    assert r2 == [7, 5, 6, 2, 4, 1, 10, 8, 9, 3]
    assert score(r2) == 291
