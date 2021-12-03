from typing import *


def part1(commands: List[str]) -> int:
    h_pos = 0
    depth = 0
    for c in commands:
        direction, num = c.split(" ")
        m = int(num)

        if direction == "forward":
            h_pos += m
        elif direction == "up":
            depth -= m
        elif direction == "down":
            depth += m
        else:
            raise ValueError()

    return h_pos * depth


def part2(commands: List[str]) -> int:
    h_pos = 0
    depth = 0
    aim = 0
    for c in commands:
        direction, num = c.split(" ")
        m = int(num)

        if direction == "forward":
            h_pos += m
            depth += aim * m
        elif direction == "up":
            aim -= m
        elif direction == "down":
            aim += m
        else:
            raise ValueError()

    return h_pos * depth
