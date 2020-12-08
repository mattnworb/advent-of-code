from typing import Tuple, List, Dict
from collections import Counter

# The boot code is represented as a text file with one instruction per line of
# text. Each instruction consists of an operation (acc, jmp, or nop) and an
# argument (a signed number like +4 or -20).
#
# - `acc` increases or decreases a single global value called the accumulator by
#   the value given in the argument. For example, acc +7 would increase the
#   accumulator by 7. The accumulator starts at 0. After an acc instruction, the
#   instruction immediately below it is executed next.
# - `jmp` jumps to a new instruction relative to itself. The next instruction to
#   execute is found using the argument as an offset from the jmp instruction;
#   for example, jmp +2 would skip the next instruction, jmp +1 would continue
#   to the instruction immediately below it, and jmp -20 would cause the
#   instruction 20 lines above to be executed next.
# - `nop` stands for No OPeration - it does nothing. The instruction immediately
#   below it is executed next.

Instruction = Tuple[str, int]
BootCode = List[Instruction]


def parse_boot_code(inp: str) -> BootCode:
    instrs: BootCode = []
    for line in inp.strip().split("\n"):
        op, arg = line.split(" ", 2)
        instrs.append((op, int(arg)))
    return instrs


class Console(object):
    def __init__(self, code: BootCode):
        self.code = code
        self.accumulator = 0
        self.ip = 0  # instruction pointer

        # track which instructions have been visited
        self.visit_order: List[int] = []
        self.count_per_instr: Dict[int, int] = Counter()
        self._track_visit()

    def _track_visit(self):
        self.visit_order.append(self.ip)
        self.count_per_instr[self.ip] += 1

    def step(self):
        op, arg = self.code[self.ip]
        if op == "acc":
            self.accumulator += arg
            self.ip += 1
        elif op == "jmp":
            self.ip += arg
        elif op == "nop":
            self.ip += 1
        else:
            raise ValueError(f"unknown op {op}")

        self._track_visit()

    def run_until_done(self) -> bool:
        """
        Run the code until terminating, or until the next instruction will cause
        an infinite loop (arriving at an instruction we've already run once).
        Return True if the code terminated normally, or False if a loop is
        encountered.
        """

        while True:
            self.step()

            # have we terminated normally?
            if self.ip == len(self.code):
                return True

            # is this next instruction a jump to a place we've already been? stop
            op, arg = self.code[self.ip]
            if op == "jmp" and self.count_per_instr[self.ip + arg] > 0:
                return False


def solve_halting_problem(original_code: BootCode) -> int:
    # make sure we have a loop first
    assert Console(original_code).run_until_done() == False

    # mutate one instruction at a time until we terminate normally
    for ix in range(len(original_code)):
        # Somewhere in the program, either a jmp is supposed to be a nop, or a
        # nop is supposed to be a jmp. (No acc instructions were harmed in the
        # corruption of this boot code.)

        code = list(original_code)
        op, arg = code[ix]
        if op == "jmp":
            code[ix] = ("nop", arg)
        elif op == "nop":
            code[ix] = ("jmp", arg)
        else:
            continue

        c = Console(code)
        normal_exit = c.run_until_done()
        if normal_exit:
            return c.accumulator

    raise ValueError("no instruction swap fixed the infinite loop")
