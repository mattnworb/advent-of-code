from typing import *


def part1(commands: List[str]) -> int:
    h_pos = 0
    depth = 0
    for c in commands:
        direction, num = c.split(" ")
        num = int(num)

        if direction == "forward":
            h_pos += num
        elif direction == "up":
            depth -= num
        elif direction == "down":
            depth += num
        else:
            raise ValueError()

    return h_pos * depth


def part2(commands: List[str]) -> int:
    h_pos = 0
    depth = 0
    aim = 0
    for c in commands:
        direction, num = c.split(" ")
        num = int(num)

        if direction == "forward":
            h_pos += num
            depth += aim * num
        elif direction == "up":
            aim -= num
        elif direction == "down":
            aim += num
        else:
            raise ValueError()

    return h_pos * depth
