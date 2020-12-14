from problem14 import *


ex1 = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""


def test_apply_mask():
    assert apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 11) == 73
    assert apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 101) == 101


def test_part1_example():
    assert computer(ex1) == 165


def test_apply_mask_v2():
    assert apply_mask_v2("000000000000000000000000000000X1001X", 42) == {26, 27, 58, 59}


ex2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


def test_part2_example():
    assert computer(ex2, version=2) == 208
