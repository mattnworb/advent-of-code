from typing import List, Tuple, Optional

import re


def is_password_valid(line: str) -> bool:
    # example:
    # 1-3 a: abcde
    req, pw = line.split(": ", 2)

    lengths, ch = req.split(" ", 2)
    min_length, max_length = map(int, lengths.split("-", 2))

    return min_length <= pw.count(ch) <= max_length


def count_valid_passwords(lines: List[str]) -> int:
    count = 0
    for line in lines:
        line = line.strip()
        if line and is_password_valid(line):
            count += 1
    return count
