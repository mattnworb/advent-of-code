from problem01 import find_sum_product


nums = [1721, 979, 366, 299, 675, 1456]


def test_pair():
    assert find_sum_product(nums, 2, 2020) == 514579


def test_triple():
    assert find_sum_product(nums, 3, 2020) == 241861950
