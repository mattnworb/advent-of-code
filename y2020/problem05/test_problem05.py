from . import *


def test_decode_seat():
    # So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

    # Every seat also has a unique seat ID: multiply the row by 8, then add the
    # column. In this example, the seat has ID 44 * 8 + 5 = 357.

    # BFFFBBFRRR: row 70, column 7, seat ID 567.
    # FFFBBBFRRR: row 14, column 7, seat ID 119.
    # BBFFBBFRLL: row 102, column 4, seat ID 820.
    assert decode_seat("FBFBBFFRLR") == (44, 5)
    assert decode_seat("BFFFBBFRRR") == (70, 7)
    assert decode_seat("FFFBBBFRRR") == (14, 7)
    assert decode_seat("BBFFBBFRLL") == (102, 4)


def test_seat_id():
    assert seat_id((44, 5)) == 357
    assert seat_id((70, 7)) == 567
    assert seat_id((14, 7)) == 119
    assert seat_id((102, 4)) == 820
