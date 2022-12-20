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


def test_compressed_graph():
    cg = compressed_graph(*parse(example))

    assert cg == {
        "BB": {"CC": 1, "DD": 2, "EE": 3, "HH": 6, "JJ": 3},
        "CC": {"BB": 1, "DD": 1, "EE": 2, "HH": 5, "JJ": 4},
        "DD": {"BB": 2, "CC": 1, "EE": 1, "HH": 4, "JJ": 3},
        "EE": {"BB": 3, "CC": 2, "DD": 1, "HH": 3, "JJ": 4},
        "HH": {"BB": 6, "CC": 5, "DD": 4, "EE": 3, "JJ": 7},
        "JJ": {"BB": 3, "CC": 4, "DD": 3, "EE": 4, "HH": 7},
    }


def test_part1_example():
    # minute 1: move to DD
    # minute 2: open to DD
    # minute 3: DD releases 20, no time left to do anything
    assert part1(example, minutes=3) == 20

    # minute 1: move to DD
    # minute 2: open to DD
    # minute 3: DD releases 20, move to EE
    # minute 4: DD releases 20, open EE
    # minute 4: DD releases 20, EE releases 3
    assert part1(example, minutes=5) == 63

    assert part1(example) == 1651


def test_part2_example():
    # minute 1: a moves to DD, b moves to BB
    # minute 2: open DD, open BB
    # minute 3: 20 + 13 released
    assert part2(example, minutes=3) == 33
    assert part2(example) == 1707
