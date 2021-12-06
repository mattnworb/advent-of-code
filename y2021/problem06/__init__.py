from typing import *
from collections import Counter

# Although you know nothing about this specific species of lanternfish, you make
# some guesses about their attributes. Surely, each lanternfish creates a new
# lanternfish once every 7 days.
#
# However, this process isn't necessarily synchronized between every lanternfish
# - one lanternfish might have 2 days left until it creates another lanternfish,
#   while another might have 4. So, you can model each fish as a single number
#   that represents the number of days until it creates a new lanternfish.
#
# Furthermore, you reason, a new lanternfish would surely need slightly longer
# before it's capable of producing more lanternfish: two more days for its first
# cycle.
#
# So, suppose you have a lanternfish with an internal timer value of 3:
#
# - After one day, its internal timer would become 2.
# - After another day, its internal timer would become 1.
# - After another day, its internal timer would become 0.
# - After another day, its internal timer would reset to 6, and it would create
#   a new lanternfish with an internal timer of 8.
# - After another day, the first lanternfish would have an internal timer of 5,
#   and the second lanternfish would have an internal timer of 7.
#
# A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0
# is included as a valid timer value). The new lanternfish starts with an
# internal timer of 8 and does not start counting down until the next day.
#
# ...
# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each
# other number decreases by 1 if it was present at the start of the day.
#
# In this example, after 18 days, there are a total of 26 fish. After 80 days,
# there would be a total of 5934.
#
# Find a way to simulate lanternfish. How many lanternfish would there be after
# 80 days?

# -------------------------------------------------------------------------
# my notes:
# use a Counter to keep track of how many fish are at each timer value
# for each day, walk through the Counter, incrementing/decrementing values


def count_fish(initial: Counter, days: int) -> int:
    c = Counter(initial)  # copy
    for _ in range(days):
        new_c: Counter[int] = Counter()
        for d in range(1, 9):  # [1, 8] - skip 0
            new_c[d - 1] = c[d]
        # fishes on day 0 move to 6
        new_c[6] += c[0]
        # and spawn new fish
        new_c[8] += c[0]
        c = new_c
    return sum(c.values())


def read_input(inp: str) -> Counter[int]:
    c: Counter[int] = Counter()
    for s in inp.split(","):
        c[int(s)] += 1
    return c


def part1(inp: str):
    return count_fish(read_input(inp), 80)


def part2(inp: str):
    return count_fish(read_input(inp), 256)
