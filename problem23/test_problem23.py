from problem23 import *


def test_part1_example():
    assert part1("389125467", rounds=10) == "92658374"
    assert part1("389125467", rounds=100) == "67384529"


def test_part2_example():
    assert part2("389125467") == 149245887792
