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
    grid = parse(inp)

    # To measure the viewing distance from a given tree, look up, down, left,
    # and right from that tree; stop if you reach an edge or at the first tree
    # that is the same height or taller than the tree under consideration. (If a
    # tree is right on the edge, at least one of its viewing distances will be
    # zero.)
    #
    # A tree's scenic score is found by multiplying together its viewing
    # distance in each of the four directions.
    #
    # Consider each tree on your map. What is the highest scenic score possible for any tree?

    # -------------

    # seems like a brute force approach of visiting every tree and measuring the score would be simplest and not too expensive

    leny = len(grid)
    lenx = len(grid[0])

    max_scenic_score = 0

    # TODO: can probably skip visiting the edges as they will have a score of 0
    for x in range(lenx):
        for y in range(leny):
            # remember - the grid position is grid[y][x] not grid[x][y]
            this_pos = grid[y][x]
            dist_up, dist_down, dist_left, dist_right = 0, 0, 0, 0

            # look up
            for ny in range(y - 1, -1, -1):
                dist_up += 1
                if this_pos <= grid[ny][x]:
                    # stop
                    break

            # look down
            for ny in range(y + 1, leny):
                dist_down += 1
                if this_pos <= grid[ny][x]:
                    # stop
                    break

            # look left
            for nx in range(x - 1, -1, -1):
                dist_left += 1
                if this_pos <= grid[y][nx]:
                    # stop
                    break

            # look right
            for nx in range(x + 1, lenx):
                dist_right += 1
                if this_pos <= grid[y][nx]:
                    # stop
                    break

            this_score = dist_up * dist_down * dist_left * dist_right
            if this_score > max_scenic_score:
                max_scenic_score = this_score

    return max_scenic_score
