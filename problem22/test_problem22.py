from problem22 import *


def test_part1_example():
    # from example:
    # Player 1's deck: 9, 2, 6, 3, 1
    # Player 2's deck: 5, 8, 4, 7, 10
    d1 = [9, 2, 6, 3, 1]
    d2 = [5, 8, 4, 7, 10]

    r1, r2 = play_game(d1, d2)
    assert r1 == []
    assert r2 == [3, 2, 10, 6, 8, 5, 9, 4, 7, 1]


def test_score():
    assert score([3, 2, 10, 6, 8, 5, 9, 4, 7, 1]) == 306
