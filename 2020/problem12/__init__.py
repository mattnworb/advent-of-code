from typing import List, Tuple

# - Action N means to move north by the given value.
# - Action S means to move south by the given value.
# - Action E means to move east by the given value.
# - Action W means to move west by the given value.
# - Action L means to turn left the given number of degrees.
# - Action R means to turn right the given number of degrees.
# - Action F means to move forward by the given value in the direction the ship is currently facing.


def part1(instr: List[str]) -> Tuple[int, int]:
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


# - Action N means to move the waypoint north by the given value.
# - Action S means to move the waypoint south by the given value.
# - Action E means to move the waypoint east by the given value.
# - Action W means to move the waypoint west by the given value.
# - Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
# - Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
# - Action F means to move forward to the waypoint a number of times equal to the given value.
def part2(instr: List[str]) -> Tuple[int, int]:
    pos = (0, 0)  # (x, y) - x = east/west, y = north/south

    # The waypoint starts 10 units east and 1 unit north relative to the ship.
    # The waypoint is relative to the ship; that is, if the ship moves, the
    # waypoint moves with it.
    waypoint = (10, -1)

    for line in instr:
        action = line[0]
        value = int(line[1:])

        if action in ["N", "E", "S", "W"]:
            waypoint = move(waypoint, action, value)

        # move X times towards the waypoint
        elif action == "F":
            w = waypoint[0] * value, waypoint[1] * value
            pos = pos[0] + w[0], pos[1] + w[1]
        # rotate the waypoint around the ship
        elif action == "R":
            assert value % 90 == 0
            # clockwise
            # example:  waypoint starts at (10, -4). R90 moves it to (4, 10).
            # a second R90 would move it to (-10, 4)
            # move 90 degrees at a time
            for _ in range(value // 90):
                x = -1 * waypoint[1]
                y = waypoint[0]
                waypoint = x, y

        elif action == "L":
            assert value % 90 == 0
            # counterclockwise
            # example: (10, -4) = east 10 north 4
            # move L90 should bring it to west 4 north 10 == (-4, -10)
            for _ in range(value // 90):
                x = waypoint[1]
                y = -1 * waypoint[0]
                waypoint = x, y

        else:
            raise ValueError("bad instruction")
    return pos
