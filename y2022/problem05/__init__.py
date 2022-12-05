from typing import *


class Stack:
    def __init__(self, iterable=None):
        if iterable:
            self.items = list(iterable)
        else:
            self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: str) -> None:
        # initial mistake here: pushing into front of list, while popping off the end
        self.items.append(item)

    def pop(self) -> str:
        return self.items.pop()

    def peek(self) -> str:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    # this is a little backwards because I am printing the list as normal, and
    # the "top" of the stack appears at the right - but it works for me
    def __repr__(self) -> str:
        return f"Stack(len={len(self.items)} items={self.items})"


# class Instruction:
#     def __init__(self, count: int, from_pos: int, to_pos: int):
#         self.count = count
#         self.from_pos = from_pos
#         self.to_pos = to_pos

Instruction = Tuple[int, int, int]


def parse(inp: str) -> Tuple[List[Stack], List[Instruction]]:
    # find break between sections
    lines = inp.split("\n")
    section_break = lines.index("")

    # read the line before the break to figure out how many stacks there are
    num_stacks = int(lines[section_break - 1].strip().split("  ")[-1])

    stacks = [Stack() for n in range(num_stacks)]

    # read from bottom up
    for line in lines[section_break - 2 :: -1]:
        # every fourth char should be a "[", like:
        # [G]     [P] [C] [F] [G] [T]
        for ix in range(0, len(line), 4):
            if line[ix] == "[":
                # next char is item
                stack_num = ix // 4
                stacks[stack_num].push(line[ix + 1])

    # now read the instructions
    instructions: List[Instruction] = []
    for line in lines[section_break + 1 :]:
        # example:
        # move 16 from 8 to 2
        tokens = line.split(" ")
        assert tokens[0] == "move"
        count = int(tokens[1])
        # instructions are one-indexed:
        from_pos = int(tokens[3]) - 1
        to_pos = int(tokens[5]) - 1
        instructions.append((count, from_pos, to_pos))

    return stacks, instructions


def part1(inp: str):
    stacks, instructions = parse(inp)

    for count, from_pos, to_pos in instructions:
        # print(f"moving {count} from {from_pos+1} to {to_pos+1}")
        assert (
            stacks[from_pos].size() >= count
        ), f"stack at index {from_pos} only has {stacks[from_pos].size()} items but attempting to remove {count}"
        assert (
            0 <= from_pos < len(stacks)
        ), f"from_pos={from_pos} out of range, stack count is {len(stacks)}"
        assert (
            0 <= to_pos < len(stacks)
        ), f"to_pos={to_pos} out of range, stack count is {len(stacks)}"
        for n in range(count):
            stacks[to_pos].push(stacks[from_pos].pop())

        # The Elves just need to know which crate will end up on top of each
        # stack; in this example, the top crates are C in stack 1, M in stack 2,
        # and Z in stack 3, so you should combine these together and give the
        # Elves the message CMZ.

    return "".join(stack.peek() for stack in stacks if not stack.is_empty())


def part2(inp: str):
    # difference between this and part1 - move batches of crates in order
    stacks, instructions = parse(inp)

    for count, from_pos, to_pos in instructions:
        # print(f"moving {count} from {from_pos+1} to {to_pos+1}")
        assert (
            stacks[from_pos].size() >= count
        ), f"stack at index {from_pos} only has {stacks[from_pos].size()} items but attempting to remove {count}"
        assert (
            0 <= from_pos < len(stacks)
        ), f"from_pos={from_pos} out of range, stack count is {len(stacks)}"
        assert (
            0 <= to_pos < len(stacks)
        ), f"to_pos={to_pos} out of range, stack count is {len(stacks)}"

        # here is the change:
        # create a new, temp Stack
        s = Stack()
        for n in range(count):
            s.push(stacks[from_pos].pop())
        for n in range(count):
            stacks[to_pos].push(s.pop())

    return "".join(stack.peek() for stack in stacks if not stack.is_empty())
