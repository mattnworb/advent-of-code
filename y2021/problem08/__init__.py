from typing import *

# Problem text:
#
# Each digit of a seven-segment display is rendered by turning on or off any of
# seven segments named a through g:
#
#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
#
# ...
#
# Because the digits 1, 4, 7, and 8 each use a unique number of segments, you
# should be able to tell which combinations of signals correspond to those
# digits. Counting only digits in the output values (the part after | on each
# line), in the above example, there are 26 instances of digits that use a
# unique number of segments (highlighted above).
#
# Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?
#
# -------------------------------------------------------------------
# My notes:
#
# number of segments by digit:
# 0: 6
# 1: 2 (unique)
# 2: 5
# 3: 5
# 4: 4 (unique)
# 5: 5
# 6: 6
# 7: 3 (unique)
# 8: 7 (unique)
# 9: 6


def part1(inp: str):
    pass


def part2(inp: str):
    pass
