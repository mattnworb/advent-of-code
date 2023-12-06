from y2023.problem05 import *

example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_part1_example():
    assert part1(example) == 35


def test_calculate_overlap():
    assert calculate_overlap(range(3), range(3, 10)) == range(0)
    assert calculate_overlap(range(3, 10), range(3)) == range(0)

    # [0,1,2] and [2]
    assert calculate_overlap(range(3), range(2, 3)) == range(2, 3)

    # one contains the other
    assert calculate_overlap(range(2, 7), range(3, 6)) == range(3, 6)
    assert calculate_overlap(range(3, 6), range(2, 7)) == range(3, 6)

    assert calculate_overlap(range(3, 6), range(4, 9)) == range(4, 6)
    assert calculate_overlap(range(4, 9), range(3, 6)) == range(4, 6)


def test_add():
    assert add(range(1, 5), 10) == range(11, 15)
    assert add(range(1, 5), 0) == range(1, 5)


def test_breakup():
    assert breakup(range(5, 8), range(0, 11)) == [range(5, 8)]

    assert breakup(range(0, 11), range(5, 8)) == [
        range(0, 5),
        range(5, 8),
        (range(8, 11)),
    ]

    assert breakup(range(1, 4), range(3, 5)) == [range(1, 3), range(3, 4)]
    assert breakup(range(3, 5), range(1, 4)) == [range(3, 4), range(4, 5)]


def test_part2_example():
    assert part2(example) == 46
