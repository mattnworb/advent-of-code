from . import *


def test_part1_example():
    # For example, suppose you know that the card's public key is 5764801. With
    # a little trial and error, you can work out that the card's loop size must
    # be 8, because transforming the initial subject number of 7 with a loop
    # size of 8 produces 5764801.
    #
    # Then, suppose you know that the door's public key is 17807724. By the same
    # process, you can determine that the door's loop size is 11, because
    # transforming the initial subject number of 7 with a loop size of 11
    # produces 17807724.
    #
    # At this point, you can use either device's loop size with the other
    # device's public key to calculate the encryption key. Transforming the
    # subject number of 17807724 (the door's public key) with a loop size of 8
    # (the card's loop size) produces the encryption key, 14897079.
    # (Transforming the subject number of 5764801 (the card's public key) with a
    # loop size of 11 (the door's loop size) produces the same encryption key:
    # 14897079.)
    assert part1("5764801\n17807724") == 14897079
