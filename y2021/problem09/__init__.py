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

    def find_low_points(self) -> List[int]:
        values = []
        for r in range(self.row_count):
            for c in range(self.col_count):
                # has to be lower than ALL neighbors
                if all(
                    self.points[r][c] < self.points[x][y]
                    for x, y in self.neighbors_of(r, c)
                ):
                    values.append(self.points[r][c])
        return values


# "Find all of the low points on your heightmap. What is the sum of the risk
# levels of all low points on your heightmap?"
def part1(inp: str):
    g = Grid(inp)
    # "The risk level of a low point is 1 plus its height"
    return sum(map(lambda a: a + 1, g.find_low_points()))


def part2(inp: str):
    pass
