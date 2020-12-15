from typing import *

# In this game, the players take turns saying numbers. They begin by taking
# turns reading from a list of starting numbers (your puzzle input). Then, each
# turn consists of considering the most recently spoken number:
#
# If that was the first time the number has been spoken, the current player says
# 0. Otherwise, the number had been spoken before; the current player announces
# how many turns apart the number is from when it was previously spoken.


def part1(inp: str, max_round: int) -> int:
    """Play the game for max_round, returning the max_round-th number spoken."""

    input_numbers = [int(n) for n in inp.strip().split(",")]

    # the dict contains the round number as keys and the number spoken as values.
    # if a number is repeated in the input, this will overwrite it.
    # only the most recent round a number was spoken will be stored.
    round_spoken = {int(num): round + 1 for round, num in enumerate(input_numbers)}

    all_nums_spoken = set(round_spoken.keys())

    # example: [0, 3, 6]
    #
    # - Turn 4: Now, consider the last number spoken, 6. Since that was the
    #   first time the number had been spoken, the 4th number spoken is 0.
    #
    # - Turn 5: Next, again consider the last number spoken, 0. Since it had
    #   been spoken before, the next number to speak is the difference between
    #   the turn number when it was last spoken (the previous turn, 4) and the
    #   turn number of the time it was most recently spoken before then (turn
    #   1). Thus, the 5th number spoken is 4 - 1, 3.
    #
    # Their question for you is: what will be the 2020th number spoken? In the
    # example above, the 2020th number spoken will be 436.

    prev_num = input_numbers[-1]
    # this is ugly, but we don't want it in the set when we check below:
    all_nums_spoken.remove(prev_num)

    for current_round in range(len(input_numbers) + 1, max_round + 1):
        # was this number spoken before?
        if prev_num not in all_nums_spoken:
            this_num = 0
        else:
            this_num = (current_round - 1) - round_spoken[prev_num]

        round_spoken[prev_num] = current_round - 1
        all_nums_spoken.add(prev_num)
        prev_num = this_num

    return prev_num
