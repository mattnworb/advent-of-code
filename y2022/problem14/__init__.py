from typing import *

Point = Tuple[int, int]
# Line = list[Point]


def line_between(a: Point, b: Point) -> Iterator[Point]:
    """Returns every point in the horizontal or vertical line between the two
    points.

    Note the returned values might not be in the same order as the parameters,
    i.e. (1,3) -> (4,3) might return (4,3), (3,3) etc."""
    assert a[0] == b[0] or a[1] == b[1]
    start = min(a[0], b[0]), min(a[1], b[1])
    end = max(a[0], b[0]), max(a[1], b[1])

    # a nested for loop here is a little silly since we know one of these will
    # only iterate over a single point (since we guarantee the points are either
    # in the same horizontal or vertical line) ... but it makes writing the code
    # easier as i don't need to figure out the orientation of the line
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            yield x, y


def move_down(p: Point) -> Point:
    # remember that the sand moving "down" means it goes from (500,0) to (500,1) etc
    return p[0], p[1] + 1


def move_down_and_left(p: Point) -> Point:
    return p[0] - 1, p[1] + 1


def move_down_and_right(p: Point) -> Point:
    return p[0] + 1, p[1] + 1


def candidate_moves(p: Point) -> Iterator[Point]:
    yield move_down(p)
    yield move_down_and_left(p)
    yield move_down_and_right(p)


def part1(inp: str):
    grid: Dict[Tuple[int, int], str] = {}

    for line in inp.split("\n"):
        endpoints = []
        for coord in line.split(" -> "):
            x, y = map(int, coord.split(","))
            endpoints.append((x, y))

        for ix, point in enumerate(endpoints[1:]):
            # add a rock for each point on the line between the endpoints
            prev = endpoints[ix]
            for x, y in line_between(prev, point):
                grid[(x, y)] = "#"

    sand_start = (500, 0)
    bottom_rock_y = max(rock[1] for rock in grid)

    falling_into_void = False

    falling_sand = sand_start

    num_resting_sands = 0

    while not falling_into_void:
        sand_moved = False
        for candidate in candidate_moves(falling_sand):
            if candidate not in grid:
                # before coming to a stop and noting position in a grid, check if we are past the lowest y-value of any rock - which means we are now falling into the void and can stop
                if falling_sand[1] >= bottom_rock_y:
                    falling_into_void = True
                    break

                # print(f"sand moving from {falling_sand} to {candidate}")
                falling_sand = candidate
                sand_moved = True
                break  # next iteration of while loop

        if falling_into_void or sand_moved:
            continue

        # "If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves..."
        assert (
            falling_sand not in grid
        ), f"can't rest at {falling_sand} because the spot is already occupied with {grid[falling_sand]}"
        grid[falling_sand] = "o"
        num_resting_sands += 1

        # "... at which point the next unit of sand is created back at the source."
        falling_sand = sand_start

    # print the grid
    minx = min(p[0] for p in grid)
    maxx = max(p[0] for p in grid)
    miny = min(p[1] for p in grid)
    maxy = max(p[1] for p in grid)

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            ch = grid[(x, y)] if (x, y) in grid else "."
            print(ch, end="")
        print()
    return num_resting_sands


def part2(inp: str):
    pass
