from typing import *


# The first order of business is to figure out how quickly the depth increases,
# just so you know what you're dealing with - you never know if the keys will
# get carried into deeper water by an ocean current or a fish or something.
#
# To do this, count the number of times a depth measurement increases from the
# previous measurement. (There is no measurement before the first measurement.)
#
# How many measurements are larger than the previous measurement?
def part1(inp: str):
    prev = None
    increases = 0
    for line in inp.split("\n"):
        cur = int(line)
        if prev is not None and cur > prev:
            increases += 1
        prev = cur
    return increases


# Considering every single measurement isn't as useful as you expected: there's
# just too much noise in the data.
#
# Instead, consider sums of a three-measurement sliding window. Again
# considering the above example:
#
# ...
#
# Start by comparing the first and second three-measurement windows. The
# measurements in the first window are marked A (199, 200, 208); their sum is
# 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum
# is 618. The sum of measurements in the second window is larger than the sum of
# the first, so this first comparison increased.
#
# Your goal now is to count the number of times the sum of measurements in this
# sliding window increases from the previous sum. So, compare A with B, then
# compare B with C, then C with D, and so on. Stop when there aren't enough
# measurements left to create a new three-measurement sum.
#
# ...
#
# Consider sums of a three-measurement sliding window. How many sums are larger
# than the previous sum?
def part2(inp: str):
    increases = 0
    this_window: List[int] = []

    measurements = [int(line) for line in inp.split("\n")]

    for ix, m in enumerate(measurements):
        # print(m)

        # copy before append
        prev_window = list(this_window)
        this_window.append(m)

        if len(this_window) > 3:
            # print("filled up this window")

            # trim
            this_window = this_window[1:]

            # print(f"comparing windows this={this_window} and prev={prev_window}")

            if len(prev_window) == 3:
                if sum(this_window) > sum(prev_window):
                    increases += 1

    return increases
