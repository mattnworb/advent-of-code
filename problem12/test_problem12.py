from problem12 import *

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
    r = make_moves(ex)
    assert r == (17, 8)
    assert manhattan_distance(r) == 25
