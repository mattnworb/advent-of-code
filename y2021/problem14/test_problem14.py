from y2021.problem14 import *

example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def test_part1_example():
    # TODO: populate
    assert part1(example) == 1588


def test_part2_example():
    assert part2(example) == 2188189693529
