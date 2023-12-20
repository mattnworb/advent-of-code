from typing import *


# (x, y) positions:
Position = tuple[int, int]
# these are really vectors
Vector = tuple[int, int]
right = (1, 0)
left = (-1, 0)
up = (0, -1)
down = (0, 1)


def add(p: Position, vector: Vector) -> Position:
    return p[0] + vector[0], p[1] + vector[1]


Beam = Tuple[Position, Vector]


def part1(inp: str):
    layout = inp.split("\n")
    max_x = len(layout[0]) - 1
    max_y = len(layout) - 1

    beams: list[Beam] = [((0, 0), right)]

    # how many tiles end up being energized?
    visited: Set[Beam] = set()

    while beams:
        pos, direction = beams.pop()
        while (
            0 <= pos[0] <= max_x
            and 0 <= pos[1] <= max_y
            and (pos, direction) not in visited
        ):
            # add here and not after add() in case the beam just left the grid
            visited.add((pos, direction))

            ch = layout[pos[1]][pos[0]]

            if ch == "/":
                if direction == right:
                    direction = up
                elif direction == left:
                    direction = down
                elif direction == up:
                    direction = right
                elif direction == down:
                    direction = left

            elif ch == "\\":
                if direction == right:
                    direction = down
                elif direction == left:
                    direction = up
                elif direction == up:
                    direction = left
                elif direction == down:
                    direction = right

            elif ch == "-" and direction in (down, up):
                direction = left
                # split - by adding another beam to process later
                beams.append((pos, right))

            elif ch == "|" and direction in (right, left):
                direction = up
                beams.append((pos, down))

            pos = add(pos, direction)

    # need to remove directions
    # visited contains every (pos, direction) tuple, we want to just count the unique positions
    return len({pos for pos, direction in visited})


def part2(inp: str):
    pass
