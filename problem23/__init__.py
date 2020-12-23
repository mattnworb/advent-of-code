from typing import *

# The small crab challenges you to a game! The crab is going to mix up some
# cups, and you have to predict where they'll end up.
#
# The cups will be arranged in a circle and labeled clockwise (your puzzle
# input). For example, if your labeling were 32415, there would be five cups in
# the circle; going clockwise around the circle from the first cup, the cups
# would be labeled 3, 2, 4, 1, 5, and then back to 3 again.
#
# Before the crab starts, it will designate the first cup in your list as the
# current cup. The crab is then going to do 100 moves.
#
# Each move, the crab does the following actions:
#
# - The crab picks up the three cups that are immediately clockwise of the
#   current cup. They are removed from the circle; cup spacing is adjusted as
#   necessary to maintain the circle.
# - The crab selects a destination cup: the cup with a label equal to the
#   current cup's label minus one. If this would select one of the cups that was
#   just picked up, the crab will keep subtracting one until it finds a cup that
#   wasn't just picked up. If at any point in this process the value goes below
#   the lowest value on any cup's label, it wraps around to the highest value on
#   any cup's label instead.
# - The crab places the cups it just picked up so that they are immediately
#   clockwise of the destination cup. They keep the same order as when they were
#   picked up.
# - The crab selects a new current cup: the cup which is immediately clockwise
#   of the current cup.
#
# ...
#
# After the crab is done, what order will the cups be in? Starting after the cup
# labeled 1, collect the other cups' labels clockwise into a single string with
# no extra characters; each number except 1 should appear exactly once. In the
# above example, after 10 moves, the cups clockwise from 1 are labeled 9, 2, 6,
# 5, and so on, producing 92658374. If the crab were to complete all 100 moves,
# the order after cup 1 would be 67384529.
#
# Using your labeling, simulate 100 moves. What are the labels on the cups after
# cup 1?


def play_game(cups: List[int], rounds: int, debug=False) -> List[int]:
    cups = list(cups)
    min_cup_label = min(cups)
    max_cup_label = max(cups)

    current = 0
    for round_num in range(1, rounds + 1):

        # instead of adjusting the index of the current item when we insert
        # things potentially before it in the list, keep track of the label
        # instead
        # current_label = cups[current]

        if debug and len(cups) == 9:
            print(f"-- move {round_num} --")
            cstr = ""
            for ix, c in enumerate(cups):
                if ix == current:
                    cstr += f"({c}) "
                else:
                    cstr += f"{c} "
            print(f"cups: {cstr}")

        # pick up 3 cups after current
        pick_up = []
        for _ in range(1, 4):
            # since we delete from the list, the position is the same on each
            # iteration
            p = (current + 1) % len(cups)
            pick_up.append(cups[p])
            del cups[p]
            if p < current:
                current -= 1

        if debug:
            print(f"pick up: {pick_up}")

        dest_label = cups[current] - 1

        if dest_label < min_cup_label:
            dest_label = max_cup_label

        while dest_label in pick_up:
            dest_label -= 1
            if dest_label < min_cup_label:
                dest_label = max_cup_label

        if debug:
            print(f"destination: {dest_label}")

        dst = cups.index(dest_label)  # TODO can we remove this index call?
        # insert into list after the destination
        cups[dst + 1 : dst + 1] = pick_up

        # we need to adjust current since we may have just inserted things before it
        if dst < current:
            current += 3

        current = (current + 1) % len(cups)

        if round_num % 1000 == 0:
            print(f"Round {round_num} done")

    return cups


def part1(inp: str, rounds=100):
    cups = list(map(int, inp))

    cups = play_game(cups, rounds)
    print(f"after {rounds} moves, cups are: {cups}")

    # this needs to start at 1 and loop back around to 1 again
    result = []
    ix = cups.index(1)
    for i in range(len(cups) - 1):
        j = (ix + i + 1) % len(cups)
        result.append(cups[j])

    return "".join(map(str, result))


def part2(inp: str):
    cups = list(map(int, inp))

    # extend the list to 1 million
    for v in range(max(cups) + 1, 1_000_000 + 1):
        cups.append(v)

    cups = play_game(cups, 10_000_000, debug=False)
    print("Game done")

    # two cups clockwise of `1`
    one_ix = cups.index(1)

    a = (one_ix + 1) % len(cups)
    b = (a + 1) % len(cups)

    return a * b
