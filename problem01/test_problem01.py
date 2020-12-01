from problem01 import find_pair


def test_simple():
    nums = [1721, 979, 366, 299, 675, 1456]
    assert find_pair(nums, 2020) == (299, 1721)
