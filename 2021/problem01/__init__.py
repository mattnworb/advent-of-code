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
