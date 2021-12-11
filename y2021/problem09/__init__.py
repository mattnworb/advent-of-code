from typing import *

# I can think of two ways to tackle part 1:
#
# 1. iterate through each position in the grid, and compare the value to its
#    above/below/left/right neighbors (if they exist). If current position is
#    lower than all neighbors, add to low point set.
#
# 2. Keep track of which positions have been visited and unvisited. For each
#    unvisited position, look at its neighbors and choose the lowest point -
#    adding each considered one to the visited set. Keep doing this from the
#    lowest neighbor until ending up at a low point / minimum. Add this to the
#    "low point" set. Keep going with unvisited positions until none left. This
#    is like testing if water can flow downhill, with the advantage that once we
#    have tested where water will flow down for a certain position or its
#    neighbor, no need to recheck later.
#
# Both seem like O(positions) so lets try 1 first.
Pos = Tuple[int, int]


class Grid:
    def __init__(self, inp: str):
        self.points = [[int(p) for p in row] for row in inp.split("\n")]
        self.row_count = len(self.points)
        self.col_count = len(self.points[0])

    def neighbors_of(self, r, c) -> Iterator[Pos]:
        if r > 0:
            yield r - 1, c
        if r < self.row_count - 1:
            yield r + 1, c
        if c > 0:
            yield r, c - 1
        if c < self.col_count - 1:
            yield r, c + 1

    def find_low_points(self) -> List[Pos]:
        positions = []
        for r in range(self.row_count):
            for c in range(self.col_count):
                # has to be lower than ALL neighbors
                if all(
                    self.points[r][c] < self.points[x][y]
                    for x, y in self.neighbors_of(r, c)
                ):
                    positions.append((r, c))
        return positions

    # (r,c) parameter is position of a low point
    def find_basin(self, r, c) -> Set[Pos]:
        assert self.points[r][c] != 9
        assert all(
            self.points[r][c] < self.points[x][y] for x, y in self.neighbors_of(r, c)
        )

        # the basin includes the low point
        basin = {(r, c)}
        visited: Set[Pos] = set()
        unvisited = {(r, c)}
        while len(unvisited) > 0:
            x, y = unvisited.pop()
            visited.add((x, y))
            for n in self.neighbors_of(x, y):
                # should we look at this pos too?
                nr, nc = n
                if self.points[nr][nc] != 9:
                    if n not in visited:
                        unvisited.add(n)
                    # test if it belongs in basin - would water flow down?
                    if self.points[nr][nc] >= self.points[x][y]:
                        basin.add(n)
        return basin


# "Find all of the low points on your heightmap. What is the sum of the risk
# levels of all low points on your heightmap?"
def part1(inp: str):
    g = Grid(inp)
    # "The risk level of a low point is 1 plus its height"
    lps = g.find_low_points()
    return sum(map(lambda v: v + 1, (g.points[r][c] for r, c in lps)))


# Next, you need to find the largest basins so you know what areas are most
# important to avoid.
#
# A basin is all locations that eventually flow downward to a single low point.
# Therefore, every low point has a basin, although some basins are very small.
# Locations of height 9 do not count as being in any basin, and all other
# locations will always be part of exactly one basin.
#
# The size of a basin is the number of locations within the basin, including the
# low point. The example above has four basins.
def part2(inp: str):

    g = Grid(inp)

    basins: List[Set[Pos]] = []
    lps = g.find_low_points()
    for r, c in lps:
        # list of points of the basin
        basins.append(g.find_basin(r, c))

    # visualize the basins
    # for basin in basins:
    #     print("basin:")
    #     for r in range(g.row_count):
    #         txt = "".join(
    #             str(g.points[r][c]) if (r, c) in basin else "x"
    #             for c in range(g.col_count)
    #         )
    #         print(txt)

    # Find the three largest basins and multiply their sizes together.
    assert len(basins) >= 3

    basins_in_desc_size = sorted(basins, key=len, reverse=True)

    return (
        len(basins_in_desc_size[0])
        * len(basins_in_desc_size[1])
        * len(basins_in_desc_size[2])
    )
