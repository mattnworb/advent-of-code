from typing import Tuple

# The first 7 characters will either be F or B; these specify exactly one of the
# 128 rows on the plane (numbered 0 through 127). Each letter tells you which
# half of a region the given seat is in. Start with the whole list of rows; the
# first letter indicates whether the seat is in the front (0 through 63) or the
# back (64 through 127). The next letter indicates which half of that region the
# seat is in, and so on until you're left with exactly one row.
#
# ...
#
# The last three characters will be either L or R; these specify exactly one of
# the 8 columns of seats on the plane (numbered 0 through 7). The same process
# as above proceeds again, this time with only three steps. L means to keep the
# lower half, while R means to keep the upper half.

ROWS = range(127)
COLS = range(8)


def decode_seat(seat: str) -> Tuple[int, int]:
    row = narrow(ROWS, seat[0:7], "F", "B")
    col = narrow(COLS, seat[7:], "L", "R")

    return (row, col)


def narrow(starting_range, moves: str, left_ch: str, right_ch: str) -> int:
    low, high = starting_range[0], starting_range[-1]
    # print(f"starting range: ({low}, {high})")
    for ch in moves:
        m = (low + high) // 2
        # print(m)

        # remembering which to add 1 to or subtract 1 or leave along I figured
        # out just by trial and error :(
        if ch == left_ch:
            high = m
        elif ch == right_ch:
            low = m + 1
        else:
            raise ValueError("bad move: " + ch)
        # print(f"saw {ch}, range changed to ({low}, {high})")

    assert low == high

    return low


def seat_id(seat: Tuple[int, int]) -> int:
    return seat[0] * 8 + seat[1]
