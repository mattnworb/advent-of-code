from typing import *
from collections import Counter


def find_reflection(pattern: List[str], ignore: int = 0) -> int:
    """Return the number of rows above the horizontal line of reflection in the pattern, or 0 if no line of reflection found."""
    midpoint = len(pattern) // 2

    for r in range(len(pattern) - 1):
        if ignore > 0 and r + 1 == ignore:
            continue
        # reflection lines fall between rows
        # if r=0, pretend the line is between rows 0 and 1 (one line is reflected)
        # loop over r testing:
        # - [r=0] if pattern[0:1] == pattern[1:0:-1] (1 line reflected)
        # - [r=1] if pattern[0:2] == pattern[3:1:-1] (2 lines reflected)
        # - [r=2] if pattern[0:3] == pattern[5:2:-1] (3 lines reflected)
        # - [r=3] if pattern[0:4] == pattern[7:3:-1] (4 lines reflected)
        # (cross over midpoint)
        # - [r=4] if pattern[2:5] == pattern[7:4:-1] (3 lines reflected)
        # - [r=5] if pattern[4:6] == pattern[7:5:-1] (2 lines reflected)
        # - [r=6] if pattern[6:7] == pattern[7:6:-1] (1 lines reflected)
        #
        # ... which generalizes to

        ref_size = min(r + 1, len(pattern) - r - 1)

        if r < midpoint:
            start1 = 0
            start2 = r + ref_size
        else:
            start1 = r + 1 - ref_size
            start2 = len(pattern) - 1

        if pattern[start1 : r + 1] == pattern[start2:r:-1]:
            return r + 1

    return 0


def summarize(pattern: List[str], ignore: int = 0) -> int:
    # check for a horizontal line of reflection (i.e. rows)
    r = find_reflection(pattern, ignore=ignore // 100)
    if r > 0:
        return r * 100

    # must be vertical line between columns
    # transpose and test again as a way of checking columns / vertical lines
    columns = []
    for c in range(len(pattern[0])):
        columns.append("".join(line[c] for line in pattern))

    return find_reflection(columns, ignore=ignore)


def part1(inp: str):
    patterns: List[List[str]] = []
    for chunk in inp.split("\n\n"):
        pattern = []
        for line in chunk.split("\n"):
            pattern.append(line)
        patterns.append(pattern)

    total = 0

    for pattern in patterns:
        s = summarize(pattern)
        assert s != 0
        total += s

    return total


def change_each_char_once(pattern: list[str]) -> Iterator[list[str]]:
    num_rows = len(pattern)
    num_cols = len(pattern[0])
    for i in range(num_rows * num_cols):
        r, c = i // num_cols, i % num_cols
        flipped_ch = "#" if pattern[r][c] == "." else "."
        new_pattern = pattern[:r]
        new_pattern.append(pattern[r][:c] + flipped_ch + pattern[r][c + 1 :])
        new_pattern.extend(pattern[r + 1 :])
        yield new_pattern


def part2(inp: str):
    patterns: List[List[str]] = []
    for chunk in inp.split("\n\n"):
        pattern = []
        for line in chunk.split("\n"):
            pattern.append(line)
        patterns.append(pattern)

    total = 0
    for pattern in patterns:
        original = summarize(pattern)
        assert original != 0

        found = False
        for candidate in change_each_char_once(pattern):
            s = summarize(candidate, ignore=original)
            if s > 0:
                found = True
                total += s
                # print(f"found new line, old={original} new={s}")
                break

        assert (
            found
        ), f"could not find smudge for pattern {pattern}, original value was {original}"

    return total
