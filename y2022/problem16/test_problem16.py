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


def test_part1_example():
    # minute 1: move to DD
    # minute 2: open to DD
    # minute 3: DD releases 20, no time left to do anything
    assert part1(example, minutes=3) == 20
    assert part1(example) == 1651


def test_part2_example():
    # minute 1: a moves to DD, b moves to BB
    # minute 2: open DD, open BB
    # minute 3: 20 + 13 released
    assert part2(example, minutes=3) == 33
    assert part2(example) == 1707
