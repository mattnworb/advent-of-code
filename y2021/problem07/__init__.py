from typing import *

# Problem:
# ...
#
# There's one major catch - crab submarines can only move horizontally.
#
# You quickly make a list of the horizontal position of each crab (your puzzle
# input). Crab submarines have limited fuel, so you need to find a way to make
# all of their horizontal positions match while requiring them to spend as
# little fuel as possible.
#
# For example, consider the following horizontal positions:
#
# 16,1,2,0,4,2,7,1,2,14 This means there's a crab with horizontal position 16, a
# crab with horizontal position 1, and so on.
#
# Each change of 1 step in horizontal position of a single crab costs 1 fuel.
# You could choose any horizontal position to align them all on, but the one
# that costs the least fuel is horizontal position 2:
#
# - Move from 16 to 2: 14 fuel
# - Move from 1 to 2: 1 fuel
# - Move from 2 to 2: 0 fuel
# - Move from 0 to 2: 2 fuel
# - Move from 4 to 2: 2 fuel
# - Move from 2 to 2: 0 fuel
# - Move from 7 to 2: 5 fuel
# - Move from 1 to 2: 1 fuel
# - Move from 2 to 2: 0 fuel
# - Move from 14 to 2: 12 fuel
#
# This costs a total of 37 fuel. This is the cheapest possible outcome; more
# expensive outcomes include aligning at position 1 (41 fuel), position 3 (39
# fuel), or position 10 (71 fuel).
#
# Determine the horizontal position that the crabs can align to using the least
# fuel possible. How much fuel must they spend to align to that position?

# -----------------------------------------------------------------------------
# My notes:
#
# is the answer to just take the mean?
# after trying: no
def total_distances(
    candidate: int, positions: List[int], cost_fn: Callable[[int, int], int]
) -> int:
    return sum(map(lambda p: cost_fn(p, candidate), positions))


def least_distance(
    positions: List[int], cost_fn: Callable[[int, int], int]
) -> Tuple[int, int]:
    # calculate initial position
    best_position = min(positions)
    least_distance = total_distances(best_position, positions, cost_fn)
    # TODO: could this be binary search?
    for candidate in range(min(positions) + 1, max(positions) + 1):
        this_total = total_distances(candidate, positions, cost_fn)
        if this_total < least_distance:
            best_position = candidate
            least_distance = this_total

    return best_position, least_distance


def parse_input(inp: str) -> List[int]:
    return list(map(int, inp.split(",")))


def pt1cost(a, b):
    return abs(a - b)


def part1(inp: str):
    positions = parse_input(inp)
    best_pos, total_dist = least_distance(positions, pt1cost)
    return total_dist


# Part 2:
#
# As it turns out, crab submarine engines don't burn fuel at a constant rate.
# Instead, each change of 1 step in horizontal position costs 1 more unit of
# fuel than the last: the first step costs 1, the second step costs 2, the third
# step costs 3, and so on.
#
# ----
# approach: parameterize the cost function


# NOTE: this could be optimized
def pt2cost(p1: int, p2: int) -> int:
    dist = abs(p1 - p2)
    return sum(range(1, dist + 1))


def part2(inp: str):
    positions = parse_input(inp)
    best_pos, total_dist = least_distance(positions, pt2cost)
    return total_dist
