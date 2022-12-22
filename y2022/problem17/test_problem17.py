from y2022.problem17 import *


def test_move_right():
    # the vertical line:
    shape = {(0, 0), (0, 1), (0, 2), (0, 3)}
    assert shape == move_right(shape, 0)

    for x in range(1, 7):
        shape = move_right(shape, 1)
        assert shape == {(x, 0), (x, 1), (x, 2), (x, 3)}

    assert shape == {(6, 0), (6, 1), (6, 2), (6, 3)}
    # can't move any more
    assert shape == move_right(shape, 1)
    assert shape == move_right(shape, 2)
    assert shape == move_right(shape, 3)
    assert shape == move_right(shape, 4)
    assert shape == move_right(shape, 5)
    assert shape == move_right(shape, 6)

    # try with a board
    shape = {(0, 0), (1, 0), (2, 0), (3, 0)}  # horizontal line
    board = {(5, 0)}  # can shift right once, but twice would be a collision
    assert move_right(shape, 1, board) == move_right(shape, 2, board)


def test_move_left():
    # the vertical line:
    shape = {(0, 0), (0, 1), (0, 2), (0, 3)}

    # can't move
    assert shape == move_left(shape, 1)

    shape = {(6, 0), (6, 1), (6, 2), (6, 3)}

    for x in range(5, -1, -1):
        shape = move_left(shape, 1)
        assert shape == {(x, 0), (x, 1), (x, 2), (x, 3)}

    assert shape == {(0, 0), (0, 1), (0, 2), (0, 3)}
    # can't move any more
    assert shape == move_left(shape, 1)
    assert shape == move_left(shape, 2)
    assert shape == move_left(shape, 3)
    assert shape == move_left(shape, 4)
    assert shape == move_left(shape, 5)
    assert shape == move_left(shape, 6)


example = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""


def test_part1_example():
    assert part1(example) == 3068


def test_part2_example():
    assert part2(example) == 1514285714288
