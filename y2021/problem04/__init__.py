from typing import *


class Board:
    def __init__(self, board_str: str):
        self.marked: Set[int] = set()
        self.nums: List[List[int]] = [
            [int(p) for p in row.split()] for row in board_str.split("\n")
        ]

    def mark(self, num: int):
        self.marked.add(num)

    def is_complete(self) -> bool:
        for row in self.nums:
            # test row
            if all(p in self.marked for p in row):
                return True
        # test col (TODO: is there an easier way?)
        for c in range(len(self.nums[0])):
            col = []
            for r in range(len(self.nums)):
                col.append(self.nums[r][c])
            if all(p in self.marked for p in col):
                return True
        return False


def part1(inp: str):
    sp = inp.split("\n\n")
    draw = sp[0]
    boards = sp[1:]
    pass


def part2(inp: str):
    pass
