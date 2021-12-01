from . import *

ex = """
F10
N3
F7
R90
F11
""".strip().split(
    "\n"
)


def test_part1_example():
    r = part1(ex)
    assert r == (17, 8)
    assert manhattan_distance(r) == 25


def test_part2():
    r = part2(ex)
    assert r == (214, 72)
