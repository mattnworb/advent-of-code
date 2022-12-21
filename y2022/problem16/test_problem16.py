import pytest

from y2022.problem16 import *

example = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


def test_mask():
    assert set_bit(0, 0) == 1
    assert is_set(set_bit(0, 0), 0)
    assert not is_set(0, 0)

    assert set_bit(0, 1) == 2
    assert is_set(2, 1)
    assert not is_set(2, 0)

    m = set_bit(0, 0)
    m = set_bit(m, 1)
    m = set_bit(m, 2)

    assert is_set(m, 0)
    assert is_set(m, 1)
    assert is_set(m, 2)
    assert not is_set(m, 3)


def test_part1_example():
    # minute 1: move to DD
    # minute 2: open to DD
    # minute 3: DD releases 20, no time left to do anything
    assert part1(example, minutes=3) == 20
    assert part1(example) == 1651


@pytest.mark.xfail
def test_part2_example():
    # TODO: populate
    assert part2(example)
