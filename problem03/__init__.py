from typing import Tuple, List

Position = Tuple[int, int]


class Map(object):
    def __init__(self, lines: List[str]):
        self.lines = lines

    def at(self, x: int, y: int) -> str:
        # wraparound
        if x >= self.cols:
            x = x % self.cols
        return self.lines[y][x]

    @property
    def rows(self) -> int:
        return len(self.lines)

    @property
    def cols(self) -> int:
        return len(self.lines[0])

    @classmethod
    def parse_map(cls, map_as_string: str):
        lines: List[str] = []
        for line in map_as_string.split("\n"):
            line = line.strip()
            if line:
                if len(lines) > 0:
                    # validate all lines are the same length
                    if len(line) != len(lines[0]):
                        raise ValueError("map does not have equal lines")
                lines.append(line)
        return cls(lines)


def count_trees(map: str, direction: Position) -> int:
    m = Map.parse_map(map)
    # starting position
    pos = (0, 0)
    tree_count = 0
    while True:
        next_pos = add(pos, direction)
        if next_pos[1] == m.rows:
            break
        if next_pos[1] > m.rows:
            print("Oops, went past bottom of map")
            break
        pos = next_pos

        val = m.at(*pos)
        # print(f"current pos={pos}: {val}")

        # are we at a tree?
        if val == "#":
            tree_count += 1

    return tree_count


def add(pos1: Position, pos2: Position) -> Position:
    return pos1[0] + pos2[0], pos1[1] + pos2[1]
