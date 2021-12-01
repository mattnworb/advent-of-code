from typing import *
import time

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


# Originally, these solutions kept state in a list, with some logic to treat it
# as circular. This is really slow for part 2, because inserting elements into
# the list at the destination cup requires finding which index that cup is at
# (with list.index(val)), and with one million elements in the list each call to
# .index(val) takes ~12 ms on my laptop to run.
#
# so instead, keep a dict from one cup to the next.
DictList = Dict[int, int]


def play_game(
    cups: List[int], rounds: int, debug=False, timing_batch=100_000
) -> DictList:
    start = time.monotonic()

    next_cup = {}
    for ix in range(len(cups)):
        next_cup[cups[ix]] = cups[(ix + 1) % len(cups)]

    min_cup_label = min(cups)
    max_cup_label = max(cups)

    current_label = cups[0]

    for round_num in range(1, rounds + 1):
        if debug and len(cups) == 9:
            print(f"-- move {round_num} --")
            cstr = ""
            c = current_label
            for _ in range(len(cups)):
                if c == current_label:
                    cstr += f"({c}) "
                else:
                    cstr += f"{c} "
                c = next_cup[c]
            print(f"cups: {cstr}")

        # pick up 3 cups after current
        pick_up = remove(next_cup, current_label, 3)

        if debug:
            print(f"pick up: {pick_up}")

        dest_label = current_label - 1

        if dest_label < min_cup_label:
            dest_label = max_cup_label

        while dest_label in pick_up:
            dest_label -= 1
            if dest_label < min_cup_label:
                dest_label = max_cup_label

        if debug:
            print(f"destination: {dest_label}")

        # insert into list after the destination
        insert(next_cup, dest_label, pick_up)

        # advance current
        current_label = next_cup[current_label]

        if round_num % timing_batch == 0:
            now = time.monotonic()
            elapsed = now - start
            # last N rounds took `elapsed`, how many are there to go?
            est = elapsed * (rounds - round_num) / timing_batch
            per_round_ms = elapsed / timing_batch * 1000
            print(
                f"Round {round_num} done, {timing_batch} rounds took {elapsed:.4f} secs, estimated completion time: {est:.2f} sec. "
                f"Time per round: {per_round_ms:.4f} ms."
            )
            start = time.monotonic()

    return next_cup


# operations on our "dict list":
def make_dict_list(nums: List[int]) -> DictList:
    state = {}
    for ix in range(len(nums)):
        state[nums[ix]] = nums[(ix + 1) % len(nums)]
    return state


def remove(d: DictList, after: int, amount: int) -> List[int]:
    """Remove `amount` numbers after the `after` label, returning them in a list"""
    new_list = []
    # perhaps this could be smarter about not re-assigning d[after] N times
    for _ in range(amount):
        # if we have <after => b => c, ...>, n is now b
        temp = d[after]
        new_list.append(temp)
        d[after] = d[temp]  # <after => c, b => c...>
        del d[temp]  # remove b => c
    return new_list


def insert(d: DictList, after: int, nums: List[int]):
    # assert all(num not in d for num in nums)

    for num in nums:
        temp = d[after]  # <after => b, b => c, ...>
        d[after] = num  # <after => num, b => c, ...> num is not in d
        d[num] = temp  # <after => num, num => b, b => c, ...>
        after = num  # next insertion point is what we just added


def dictlist_to_str(d: DictList, start: int = None, sep=" ") -> str:
    if not start:
        start = next(iter(d.keys()))
    cur = start
    s = ""
    while True:
        s += f"{cur}{sep}"
        cur = d[cur]
        if cur == start:
            break
    return s


def part1(inp: str, rounds=100, debug=False) -> str:
    cups = list(map(int, inp))

    result = play_game(cups, rounds, debug=debug)

    print(f"after {rounds} moves, cups are: {dictlist_to_str(result)}")

    s = ""
    c = result[1]
    while c != 1:
        s += f"{c}"
        c = result[c]
    return s


def part2(inp: str) -> int:
    cups = list(map(int, inp))

    # extend the list to 1 million
    now = time.monotonic()
    for v in range(max(cups) + 1, 1_000_000 + 1):
        cups.append(v)
    elapsed = time.monotonic() - now
    print(f"Took {elapsed:.2f} secs to add one million items to the cups list")

    result = play_game(cups, 10_000_000, debug=False, timing_batch=1_000_000)
    print("Game done")

    # two cups clockwise of `1`
    one_ix = cups.index(1)

    a = result[1]
    b = result[a]

    return a * b
