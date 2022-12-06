from y2021.problem15 import *

small_example = """
873
128
342""".strip()


def test_shortest_path():
    # cost = 1 + 2 + 4 + 2 = 9
    assert shortest_path(small_example) == [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]


def test_total_risk():
    m = parse(small_example)
    path = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
    assert total_risk(m, path) == 9


example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


def test_part1_example():
    assert part1(example) == 40


def test_part2_example():
    # TODO: populate
    assert part2(example)
