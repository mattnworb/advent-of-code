from typing import *


# The handshake used by the card and the door involves an operation that
# transforms a subject number. To transform a subject number, start with the
# value 1. Then, a number of times called the loop size, perform the following
# steps:
#
# - Set the value to itself multiplied by the subject number.
# - Set the value to the remainder after dividing the value by 20201227.
#
# The card always uses a specific, secret loop size when it transforms a subject
# number. The door always uses a different, secret loop size.
#
# The cryptographic handshake works like this:
#
# - The card transforms the subject number of 7 according to the card's secret
#   loop size. The result is called the card's public key.
# - The door transforms the subject number of 7 according to the door's secret
#   loop size. The result is called the door's public key.
# - The card and door use the wireless RFID signal to transmit the two public
#   keys (your puzzle input) to the other device. Now, the card has the door's
#   public key, and the door has the card's public key. Because you can
#   eavesdrop on the signal, you have both public keys, but neither device's
#   loop size.
# - The card transforms the subject number of the door's public key according to
#   the card's loop size. The result is the encryption key.
# - The door transforms the subject number of the card's public key according to
#   the door's loop size. The result is the same encryption key as the card
#   calculated.
#
# If you can use the two public keys to determine each device's loop size, you
# will have enough information to calculate the secret encryption key that the
# card and door use to communicate; this would let you send the unlock command
# directly to the door!
#
# For example, suppose you know that the card's public key is 5764801. With a
# little trial and error, you can work out that the card's loop size must be 8,
# because transforming the initial subject number of 7 with a loop size of 8
# produces 5764801.
#
# Then, suppose you know that the door's public key is 17807724. By the same
# process, you can determine that the door's loop size is 11, because
# transforming the initial subject number of 7 with a loop size of 11 produces
# 17807724.
#
# At this point, you can use either device's loop size with the other device's
# public key to calculate the encryption key. Transforming the subject number of
# 17807724 (the door's public key) with a loop size of 8 (the card's loop size)
# produces the encryption key, 14897079. (Transforming the subject number of
# 5764801 (the card's public key) with a loop size of 11 (the door's loop size)
# produces the same encryption key: 14897079.)
#
# What encryption key is the handshake trying to establish?


def transform(subject: int) -> Iterator[int]:
    val = 1

    while True:
        val *= subject
        val = val % 20201227
        yield val


def transform_n_times(subject: int, loop_size: int) -> int:
    # x = 0
    # gen = transform(subject)
    # for _ in range(loop_size):
    #     x = next(gen)
    # return x

    # From the documentation for `pow(base, exp[, mod])`:
    #
    # Return base to the power exp; if mod is present, return base to the power
    # exp, modulo mod (computed more efficiently than `pow(base, exp) % mod`).
    # The two-argument form pow(base, exp) is equivalent to using the power
    # operator: base**exp.
    #
    # How much faster is this? Cuts the run time for part1() down from ~8.7s to
    # ~4.2s.
    return pow(subject, loop_size, 20201227)


def part1(inp: str) -> int:

    card_pub_key, door_pub_key = map(int, inp.strip().split("\n"))

    # what loop size would have generated the two pub keys?
    card_loop_size = None
    door_loop_size = None
    loops = 1
    gen = transform(7)
    while True:
        next_val = next(gen)

        if next_val == card_pub_key:
            card_loop_size = loops
            print(f"determined card loop size: {card_loop_size}")

        if next_val == door_pub_key:
            door_loop_size = loops
            print(f"determined door loop size: {door_loop_size}")

        loops += 1

        if card_loop_size is not None and door_loop_size is not None:
            break

    # once we know both loop sizes, we can calculate the encryption key

    #  The card transforms the subject number of the door's public key according
    #  to the card's loop size. The result is the encryption key.
    enc_key = transform_n_times(door_pub_key, card_loop_size)

    # The door transforms the subject number of the card's public key according
    # to the door's loop size. The result is the same encryption key as the card
    # calculated.
    enc_key2 = transform_n_times(card_pub_key, door_loop_size)

    assert enc_key == enc_key2

    return enc_key
