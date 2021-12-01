from problem02 import *


lines = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".split(
    "\n"
)


def test_part1():
    assert count_valid_passwords_v1(lines) == 2


def test_part2():
    assert count_valid_passwords_v2(lines) == 1
