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

    def all_unmarked(self) -> Set[int]:
        return set([p for row in self.nums for p in row if p not in self.marked])


def part1(inp: str):
    sp = inp.split("\n\n")
    draw = sp[0]
    boards = [Board(s) for s in sp[1:]]

    for num in (int(n) for n in draw.split(",")):
        for b in boards:
            b.mark(num)

        winner = None
        for b in boards:
            if b.is_complete():
                assert winner is None, "Should be only one winner"
                winner = b
        if winner is not None:
            return sum(winner.all_unmarked()) * num

    return -1


def part2(inp: str):
    pass
