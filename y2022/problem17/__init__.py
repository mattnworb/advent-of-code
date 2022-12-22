from typing import *


# first thoughts: represent the "rocks" - positions on the board occupied by
# the tetris pieces - as (x,y) tuples in a set, so that the board (set)
# contains just the rock's positions. treat the bottom row of the board as
# y=0, row above that as y=1, etc, so that as we add rows there is nothing
# to adjust in the existing pieces/positions.
#
# represent the Tetris pieces as sets also, with rock coordinates relative to the bottom-left corner as (0, 0)
Rock = Tuple[int, int]
Shape = Set[Rock]


def shapes() -> Iterator[Shape]:
    while True:
        # the #### piece:
        yield {(0, 0), (1, 0), (2, 0), (3, 0)}
        # the cross:
        yield {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)}
        # the backwards L:
        yield {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}
        # the vertical line:
        yield {(0, 0), (0, 1), (0, 2), (0, 3)}
        # the square:
        yield {(0, 0), (1, 0), (0, 1), (1, 1)}


def move_right(shape: Shape, times: int = 1, board: Set[Rock] = set()):
    """Adjust the coordinates of the shape so that it moves right `times` time, but not past the edge of the wall"""
    max_x = max(x for x, y in shape)
    # cannot move the right-most part of the shape past a value of 6, since the x-axis is bounded between [0,6]:

    # if right-most pos is 6 and times is 1, should adjust times to 0
    # if right-most pos is 5 and times is 2, should adjust times to 1
    times = min(times, 6 - max_x)
    if times <= 0:
        return shape

    for n in range(times):
        # is anything blocking us?
        s = {(x + 1, y) for x, y in shape}
        if all((x, y) not in board for x, y in s):
            shape = s
        else:
            break
    return shape


def move_left(shape: Shape, times: int = 1, board: Set[Rock] = set()):
    """Adjust the coordinates of the shape so that it moves left `times` time, but not past the edge of the wall"""
    min_x = min(x for x, y in shape)
    # cannot move the left-most part of the shape past a value of 0, since the x-axis is bounded between [0,6]:

    # if right-most pos is 0 and times is 1, should adjust times to 0
    # if right-most pos is 1 and times is 2, should adjust times to 1
    times = min(times, min_x)
    if times <= 0:
        return shape
    for n in range(times):
        # is anything blocking us?
        s = {(x - 1, y) for x, y in shape}
        if all((x, y) not in board for x, y in s):
            shape = s
        else:
            break
    return shape


def parse_input(inp) -> Iterator[str]:
    while True:
        for ch in inp:
            yield ch


def solve(inp: str, number_of_rocks: int) -> int:

    board: Set[Rock] = set()
    max_height = 0

    # The tall, vertical chamber is exactly seven units wide. Each rock appears
    # so that its left edge is two units away from the left wall and its bottom
    # edge is three units above the highest rock in the room (or the floor, if
    # there isn't one).

    shape_gen = shapes()
    jet_gen = parse_input(inp)

    for rock_num in range(number_of_rocks):
        # new rock
        shape = next(shape_gen)
        # Each rock appears so that its left edge is two units away from the
        # left wall and its bottom edge is three units above the highest rock in
        # the room (or the floor, if there isn't one).
        shape = move_right(shape, 2)
        shape = {(x, y + max_height + 3) for x, y in shape}

        # After a rock appears, it alternates between being pushed by a jet of
        # hot gas one unit (in the direction indicated by the next symbol in the
        # jet pattern) and then falling one unit down. If any movement would
        # cause any part of the rock to move into the walls, floor, or a stopped
        # rock, the movement instead does not occur. If a downward movement
        # would have caused a falling rock to move into the floor or an
        # already-fallen rock, the falling rock stops where it is (having landed
        # on something) and a new rock immediately begins falling.

        rock_is_moving = True

        while rock_is_moving:
            jet = next(jet_gen)
            shape = (
                move_right(shape, board=board)
                if jet == ">"
                else move_left(shape, board=board)
            )

            # can we move down? only if there are no rocks in the position below these rocks, and we are not at the floor
            can_move_down = all(
                (r[0], r[1] - 1) not in board and r[1] - 1 >= 0 for r in shape
            )
            if can_move_down:
                shape = {(r[0], r[1] - 1) for r in shape}
            else:
                # if not, this rock rests
                for rock in shape:
                    assert (
                        rock not in board
                    ), f"collision after rock number {rock_num} came to rest"
                    board.add(rock)
                rock_is_moving = False
                max_height = max(max_height, max(y for x, y in shape) + 1)

    return max_height


def part1(inp: str) -> int:
    return solve(inp, 2022)


def part2(inp: str):
    return solve(inp, 1000000000000)
