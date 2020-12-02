from problem02 import count_valid_passwords


lines = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


def test_part1():
    assert count_valid_passwords(lines.split("\n")) == 2
