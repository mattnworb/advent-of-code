from typing import List, Tuple

# - Action N means to move north by the given value.
# - Action S means to move south by the given value.
# - Action E means to move east by the given value.
# - Action W means to move west by the given value.
# - Action L means to turn left the given number of degrees.
# - Action R means to turn right the given number of degrees.
# - Action F means to move forward by the given value in the direction the ship is currently facing.


def make_moves(instr: List[str]) -> Tuple[int, int]:
    pos = (0, 0)  # (x, y) - x = east/west, y = north/south
    direction = 90  # degrees, clockwise

    for line in instr:
        action = line[0]
        value = int(line[1:])

        # print(f"start: p={pos} d={direction}, next is {line}")

        if action in ["N", "E", "S", "W"]:
            pos = move(pos, action, value)
        elif action == "L":
            assert value % 90 == 0
            # print(f"turn: {action} from {direction}")
            direction = (direction - value) % 360
        elif action == "R":
            assert value % 90 == 0
            # print(f"turn: {action} from {direction}")
            direction = (direction + value) % 360
        elif action == "F":
            assert 0 <= direction < 360
            if direction == 0:
                pos = move(pos, "N", value)
            elif direction == 90:
                pos = move(pos, "E", value)
            elif direction == 180:
                pos = move(pos, "S", value)
            elif direction == 270:
                pos = move(pos, "W", value)
        else:
            raise ValueError("unkonwn action")
        # print()
    return pos


def move(pos: Tuple[int, int], action: str, value: int) -> Tuple[int, int]:

    if action == "N":
        r = pos[0], pos[1] - value
    elif action == "S":
        r = pos[0], pos[1] + value
    elif action == "E":
        r = pos[0] + value, pos[1]
    elif action == "W":
        r = pos[0] - value, pos[1]
    else:
        raise ValueError("unkonwn action")

    # print(f"move: from {pos} {action} {value} to {r}")
    return r


def manhattan_distance(pos: Tuple[int, int]) -> int:
    return abs(pos[0]) + abs(pos[1])
