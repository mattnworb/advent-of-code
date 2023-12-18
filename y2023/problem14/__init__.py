from typing import *


def move_rocks_and_score(line: str) -> int:
    size = len(line)

    # example:
    # .O...#O..O

    # scan through the line, counting how many round rocks (O) or empty spaces
    # (.) we find until we hit a cube-shaped rock (#) once we hit a #, we can
    # calculate that all the round rocks would move left as far as they can
    num_round, last_cube = 0, -1
    score = 0
    for i in range(size):
        if line[i] == "#":
            # update score
            # ..O#.O would become O..#.O
            # last_cube=0, num_round=1, score += 6
            # sum(range(size,size-num_round,-1))
            # O..#.O would become O..#O.
            # last_cube=3, num_round=1, score += 2
            # sum(range(size-(last_cube+1),size-(last_cube+1)-num_round),-1)
            # if last_cube > 0:
            score += sum(
                range(size - (last_cube + 1), size - (last_cube + 1) - num_round, -1)
            )

            last_cube = i
            num_round = 0

        elif line[i] == "O":
            num_round += 1

    # update one last time after the line terminates
    score += sum(range(size - (last_cube + 1), size - (last_cube + 1) - num_round, -1))

    return score


def spin_once(grid: list[str]) -> list[str]:
    columns = []
    for c in range(len(grid[0])):
        columns.append("".join(line[c] for line in grid))
    return columns


def part1(inp: str):
    grid: List[str] = []
    for line in inp.split("\n"):
        grid.append(line)

    # transpose as its easier to work with left to right scanning one row at a time
    grid = spin_once(grid)

    return sum(map(move_rocks_and_score, grid))


def part2(inp: str):
    # This process should work if you leave it running long enough, but you're
    # still worried about the north support beams. To make sure they'll survive
    # for a while, you need to calculate the total load on the north support
    # beams after 1000000000 cycles.
    pass
