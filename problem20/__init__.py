from typing import *
from collections import Counter, defaultdict
from functools import reduce
from operator import mul

Tile = List[str]
Position = Tuple[int, int]
Image = Dict[Position, Tile]

# some thoughts on an approach:
#
# only the borders of each tile matter
#
# since the border of one tile and the border of the tile next to it have to be
# equal, we can count how often each border (which is just a string) occurs in
# the total set of tiles.
#
# any border that only occurs once must be on the edge of the original image
# with everything put together
#
# if a tile has two borders that only occur once - is that a corner piece? No,
# because the tile could be flipped (horizontally or vertically), which means
# some "borders" are never actually used / matched up with other tiles.
#
# But from inspecting the data, there are only four tiles that have 3 unique
# borders - which seems like those must be the corner pieces.
def part1(inp: str) -> int:
    tiles = parse_input(inp)

    # dict of border (string) to count (int)
    border_counts = Counter(b for t in tiles.values() for b in borders(t))

    corner_tile_nums: Set[int] = set()

    for tile_num, tile in tiles.items():
        # count how many times each border appears once
        c = sum(1 for b in borders(tile) if border_counts[b] == 1)
        # print(f"tile {tile_num} has unique borders: {c}")
        if c >= 3:
            print(f"found corner tile: {tile_num}")
            corner_tile_nums.add(tile_num)

    assert len(corner_tile_nums) == 4

    return reduce(mul, corner_tile_nums)


def parse_input(inp: str) -> Dict[int, Tile]:
    tiles: Dict[int, Tile] = {}
    for section in inp.strip().split("\n\n"):
        lines = section.split("\n")
        # first line should be like "Tile <num>:"
        assert lines[0].startswith("Tile ")
        num = lines[0].split(" ")[1].replace(":", "")
        tiles[int(num)] = lines[1:]
    return tiles


# TODO: rename
def borders(tile: Tile) -> List[str]:
    left = "".join([t[0] for t in tile])
    right = "".join([t[-1] for t in tile])

    return [
        # top
        tile[0],
        # bottom
        tile[-1],
        # left side
        left,
        # right side
        right,
        # top reversed (if flipped)
        tile[0][::-1],
        # bottom reversed (if flipped)
        tile[-1][::-1],
        # left and right reversed
        left[::-1],
        right[::-1],
    ]


def rotate_clockwise(tile: Tile, times=1) -> Tile:
    times = times % 4

    if times == 0:
        return tile

    # input:
    # a1 a2 a3
    # b1 b2 b3
    # c1 c2 c3
    #
    # becomes:
    # c1 b1 a1
    # c2 b2 a2
    # c3 b3 a3

    len_y = len(tile)
    len_x = len(tile[0])

    for _ in range(times):
        new_tile = []
        for x in range(len_x):
            s = ""
            for y in range(len_y - 1, -1, -1):
                s += tile[y][x]
            new_tile.append(s)
        tile = new_tile

    return new_tile


def flip_y(tile: Tile) -> Tile:
    # abc    becomes:    ghi
    # def                fed
    # ghi                abc
    return tile[::-1]


def flip_x(tile: Tile) -> Tile:
    return [row[::-1] for row in tile]


def top_border(tile: Tile) -> str:
    return tile[0]


def bottom_border(tile: Tile) -> str:
    return tile[-1]


def right_border(tile: Tile) -> str:
    return "".join([t[-1] for t in tile])


def left_border(tile: Tile) -> str:
    return "".join([t[0] for t in tile])


def simple_borders(tile: Tile) -> Iterator[str]:
    yield top_border(tile)
    yield right_border(tile)
    yield bottom_border(tile)
    yield left_border(tile)


def transformations(tile: Tile, include_flip=True) -> Iterator[Tile]:
    """Return an iterator containing all possible oridentations and rotations of the tile."""
    yield tile
    yield rotate_clockwise(tile, times=1)
    yield rotate_clockwise(tile, times=2)
    yield rotate_clockwise(tile, times=3)

    if include_flip:
        flipped = flip_y(tile)
        yield flipped
        yield rotate_clockwise(flipped, times=1)
        yield rotate_clockwise(flipped, times=2)
        yield rotate_clockwise(flipped, times=3)


def part2(inp: str) -> int:
    tiles = parse_input(inp)

    # this was the output of part1
    corner_tile_nums = {3343, 3821, 3677, 3709}

    # dict of border (string) to count (int)
    border_counts = Counter(b for t in tiles.values() for b in borders(t))

    counts_per_tile: Dict[int, Dict[str, int]] = {}

    # for each tile, count how often its borders occur in the total set of borders
    for tile_num, tile in tiles.items():
        counts_per_tile[tile_num] = Counter()
        for b in borders(tile):
            counts_per_tile[tile_num][b] += border_counts[b]

    # for each tile, we now have a Counter of how often each border occurs in
    # the total set, like {"border1": 1, "border2", 4, ...}

    # now, within each tile, reduce that Counter of string to int to a Counter
    # of how many borders in that tile occur like {2:1, 6:1} meaning the tite
    # has 7 (potential) borders that occur twice and 1 that occurs 5 times
    # for tile_num, c in counts_per_tile.items():
    #     print(f"{tile_num}: {Counter(c.values())}", end="")
    #     if tile_num in corner_tile_nums:
    #         print("   (corner!)", end="")
    #     print()

    # interesting that only the corner tiles have this pattern:
    #
    # {2: 4, 1: 3, 4: 1}

    border_to_tile: Dict[str, Set[int]] = defaultdict(set)
    for tile_num, tile in tiles.items():
        for b in borders(tile):
            border_to_tile[b].add(tile_num)

    # TODO: pick one corner arbitrarily. Rotate the image until the 2
    # connections are on the right and bottom side, which lets us treat this
    # tile as (0, 0) if we were to make a two-dimensional grid of where all the
    # tiles are to end up in the larger image. We can then add the next tile
    # that connects to these two pieces, simiarly rotating it until the
    # connection is on the intended side.
    start_corner_num = 3343

    # safety check - the corner tile has connections on just two sides
    assert {2: 2, 1: 2} == Counter(
        border_counts[b] for b in simple_borders(tiles[start_corner_num])
    )

    image: Image = {}
    image_tile_nums: Dict[Position, int] = {}
    pos = (0, 0)
    # figure out which way to orient this tile to place it in the top-left corner
    for t, rotated_tile in enumerate(
        transformations(tiles[start_corner_num], include_flip=False)
    ):
        if (
            border_counts[right_border(rotated_tile)] == 2
            and border_counts[bottom_border(rotated_tile)] == 2
        ):
            print(
                f"rotated corner tile 3343 {t} times to make it fit in top left corner"
            )

            image[pos] = rotated_tile
            image_tile_nums[pos] = start_corner_num
            break
    else:
        raise ValueError("couldn't fit corner 1 into top-left position")

    # now we march on from this tile right-ward to fill the next 11 tiles
    for x in range(11):
        # the variable `pos` now refers to the previous position
        this_pos = pos[0] + 1, pos[1]
        border_to_match = right_border(image[pos])

        # which tile also has this border? check the dict containing the set of
        # tile nums with this border, and remove the tile num we've already
        # placed
        s = border_to_tile[border_to_match] - {image_tile_nums[pos]}
        assert len(s) == 1
        next_tile_num = s.pop()
        print(f"from tile {image_tile_nums[pos]}, right connection is: {next_tile_num}")

        # we know which tile has the matching border, but we have to figure out how to rotate/orient it
        for candidate in transformations(tiles[next_tile_num]):
            if left_border(candidate) == border_to_match:
                print(
                    f"found matching rotation/orientation, placing {next_tile_num} to right of {image_tile_nums[pos]}"
                )
                image[this_pos] = candidate
                image_tile_nums[this_pos] = next_tile_num
                break
        else:
            raise ValueError(
                f"couldn't rotate/flip tile {next_tile_num} to make it fit"
            )

        pos = this_pos

    print(f"done with first row, image so far is: {image_tile_nums}")

    return 0
