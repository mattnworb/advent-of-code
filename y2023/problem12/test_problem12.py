from y2023.problem12 import *

example = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def test_part1_simple():
    assert part1("# 1") == 1
    assert part1("# 0") == 0
    assert part1(". 0") == 1
    assert part1("? 1") == 1

    assert part1(".# 1") == 1
    assert part1("#. 1") == 1

    assert part1("#.# 1,1") == 1

    assert part1("?? 1") == 2
    assert part1("#? 2") == 1
    assert part1(".? 1") == 1


def test_part1_example():
    # assert part1("?#?#?#?#?#?#?#? 1,3,1,6") == 10
    assert part1(example) == 21


def test_part2_example():
    assert part2(example) == 525152
