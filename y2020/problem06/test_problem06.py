from . import *

ex1 = """
abcx
abcy
abcz
"""

ex2 = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def test_part1_example():
    assert count_groups(ex1) == 6
    assert count_groups(ex2) == 11


def test_part2_example():
    assert count_groups(ex1, intersect=True) == 3
    assert count_groups(ex2, intersect=True) == 6
