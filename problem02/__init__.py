from typing import List, Tuple, Optional

import re


def is_password_valid_v1(line: str) -> bool:
    # example:
    # 1-3 a: abcde
    req, pw = line.split(": ", 2)

    lengths, ch = req.split(" ", 2)
    min_length, max_length = map(int, lengths.split("-", 2))

    return min_length <= pw.count(ch) <= max_length


def count_valid_passwords_v1(lines: List[str]) -> int:
    count = 0
    for line in lines:
        line = line.strip()
        if line and is_password_valid_v1(line):
            count += 1
    return count


def is_password_valid_v2(line: str) -> bool:
    # example:
    # 1-3 a: abcde
    req, pw = line.split(": ", 2)

    positions, ch = req.split(" ", 2)
    pos1, pos2 = map(int, positions.split("-", 2))

    # Each policy actually describes two positions in the password, where 1 means
    # the first character, 2 means the second character, and so on. (Be careful;
    # Toboggan Corporate Policies have no concept of "index zero"!)
    #
    # "Exactly one of these positions must contain the given letter."

    # xor
    return (pw[pos1 - 1] == ch) != (pw[pos2 - 1] == ch)


def count_valid_passwords_v2(lines: List[str]) -> int:
    count = 0
    for line in lines:
        line = line.strip()
        if line and is_password_valid_v2(line):
            count += 1
    return count
