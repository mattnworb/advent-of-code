from . import *

from functools import reduce

if __name__ == "__main__":
    with open("y2020/problem03/input") as f:
        inp = f.read(-1).strip()

    print("part 1:", count_trees(inp, (3, 1)))

    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [count_trees(inp, slope) for slope in slopes]
    product = reduce(lambda a, b: a * b, trees)
    print("part 2:", product)
