from problem23 import *


def test_part1_example():
    assert part1("389125467", rounds=10, debug=True) == "92658374"
    assert part1("389125467", rounds=100) == "67384529"


def test_part2_example():
    assert part2("389125467") == 149245887792


def test_make_dict_list():
    nums = list(map(int, "389125467"))
    d = make_dict_list(nums)
    assert d == {3: 8, 8: 9, 9: 1, 1: 2, 2: 5, 5: 4, 4: 6, 6: 7, 7: 3}

    insert(d, 9, [11, 12, 13])
    assert d[8] == 9
    assert d[9] == 11
    assert d[11] == 12
    assert d[12] == 13
    assert d[13] == 1

    # test wraparound
    assert remove(d, 6, 3) == [7, 3, 8]
    assert d[6] == 9
    assert d[9] == 11
