from typing import *

Grid = List[List[int]]
Position = Tuple[int, int]


def parse(inp: str) -> Grid:
    grid = []
    for line in inp.strip().split("\n"):
        grid.append([int(ch) for ch in line])
    return grid


def part1(inp: str):
    # Consider your map; how many trees are visible from outside the grid?

    # idea: might not need to know/store the visibility status for every
    # position in the grid, but just the count
    #
    # so could walk through the grid, and e.g. while walking right (seeing what
    # is visible from left), increment a counter each time current_pos >
    # max_pos_seen_so_far
    #
    # ........
    # 3245....
    #
    # by the time you reach 5, we know there are now 3 visible trees (from the
    # left) in this row so far (3, 4, 5). then do same count starting at right
    # and moving left this would require scanning each row twice, and each
    # column twice
    #
    # as opposed to for each position, walking in all four directions until
    # reaching either the edge or a tree taller than it (if found edge and
    # nothing taller, is visible, if found something taller before edge, is not
    # visible). this requires more iterating ... but maybe not a ton more? for
    # each position, you scan at worst the entire row + column

    grid = parse(inp)

    visible_trees: Set[Position] = set()

    leny = len(grid)
    lenx = len(grid[0])

    # visit each row
    for y, row in enumerate(grid):
        # left to right
        maxh = row[0]
        for x in range(lenx):
            if x == 0 or x == (lenx - 1):
                visible_trees.add((x, y))
            elif row[x] > maxh:
                maxh = row[x]
                visible_trees.add((x, y))

        # right to left
        maxh = row[-1]
        # stop=0 b/c we can skip left edge as we've already added it
        for x in range(lenx - 1, 0, -1):
            if row[x] > maxh:
                maxh = row[x]
                visible_trees.add((x, y))

    # visit each column
    for x in range(lenx):
        col = [grid[y][x] for y in range(leny)]
        # top to bottom
        maxh = col[0]
        for y in range(leny):
            if y == 0 or y == (leny - 1):
                visible_trees.add((x, y))
            elif col[y] > maxh:
                maxh = col[y]
                visible_trees.add((x, y))

        # bottom to top
        maxh = col[-1]
        for y in range(leny - 1, 0, -1):
            if col[y] > maxh:
                maxh = col[y]
                visible_trees.add((x, y))

    return len(visible_trees)


def part2(inp: str):
    pass
