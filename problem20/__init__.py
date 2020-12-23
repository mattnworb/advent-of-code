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
# But from inspecting the data after counting how often each border string
# occurs, and what those counts look like in each tile ...  there are only four
# tiles that have 3 unique borders - which seems like those must be the corner
# pieces. This means we don't have to actually assemble the whole image out of
# all of the tiles for this part.
def part1(inp: str) -> int:
    tiles = parse_input(inp)

    # dict of border (string) to count (int)
    border_counts = Counter(b for t in tiles.values() for b in all_borders(t))

    corner_tile_nums: Set[int] = set()

    for tile_num, tile in tiles.items():
        # count how many times each border appears once
        c = sum(1 for b in all_borders(tile) if border_counts[b] == 1)
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


def all_borders(tile: Tile) -> Iterator[str]:
    """Return the eight distinct borders for the Tile after rotations/flips."""

    yield top_border(tile)
    yield bottom_border(tile)
    yield left_border(tile)
    yield right_border(tile)

    # when we flip the tile on the x or y axis, two of the borders are the same
    # as before, depending on which axis we did
    fx, fy = flip_x(tile), flip_y(tile)

    yield top_border(fx)
    yield bottom_border(fx)
    yield left_border(fy)
    yield right_border(fy)


# To solve part 2, we'll need to actually assemble all the tiles into one image.
# For that, we need to define rotation and flip operations:


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
    """Return an iterator containing all possible orientations and rotations of the tile."""
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


def assert_image_valid(image: Image):
    max_x, max_y = max(image.keys())

    # for each position, check that the neighboring tiles have matching borders
    for p, tile in image.items():
        x, y = p

        if x > 0:
            q = x - 1, y
            assert left_border(tile) == right_border(
                image[q]
            ), f"left border of {p} does not match right border of {q}: {left_border(tile)} != {right_border(image[q])}"

        if y > 0:
            q = x, y - 1
            assert top_border(tile) == bottom_border(
                image[q]
            ), f"top border of {p} does not match bottom border of {q}: {top_border(tile)} != {bottom_border(image[q])}"

        if x < max_x - 1:
            q = x + 1, y
            assert right_border(tile) == left_border(
                image[q]
            ), f"right border of {p} does not match left border of {q}: {right_border(tile)} != {left_border(image[q])}"

        if y < max_y - 1:
            q = x, y + 1
            assert bottom_border(tile) == top_border(
                image[q]
            ), f"bottom border of {p} does not match top border of {q}: {bottom_border(tile)} != {top_border(image[q])}"


def assemble_image(
    tiles: Dict[int, Tile], corner_tile_nums: Set[int]
) -> Tuple[Image, Dict[Position, int]]:

    # dict of border (string) to count (int)
    border_counts = Counter(b for t in tiles.values() for b in all_borders(t))

    # keep track of which tiles contain each border - we'll use this later to
    # find the next tile to place based on the last placed tile, since the sides
    # have to match up.
    border_to_tile: Dict[str, Set[int]] = defaultdict(set)
    for tile_num, tile in tiles.items():
        for b in all_borders(tile):
            border_to_tile[b].add(tile_num)

    # Pick one corner arbitrarily. Rotate the image until the 2 connections are
    # on the right and bottom side, which lets us treat this tile as (0, 0) if
    # we were to make a two-dimensional grid of where all the tiles are to end
    # up in the larger image.
    start_corner_num = next(iter(corner_tile_nums))

    # safety check - the corner tile has connections on just two sides
    assert {2: 2, 1: 2} == Counter(
        border_counts[b] for b in simple_borders(tiles[start_corner_num])
    )

    image: Image = {}
    image_tile_nums: Dict[Position, int] = {}

    # Next, figure out which way to orient this tile to place it in the top-left
    # corner (so that its borders which other tiles share are at the bottom and
    # right side).
    for t, rotated_tile in enumerate(
        transformations(tiles[start_corner_num], include_flip=False)
    ):
        if (
            border_counts[right_border(rotated_tile)] == 2
            and border_counts[bottom_border(rotated_tile)] == 2
        ):
            print(
                f"rotated corner tile {start_corner_num} {t} times to make it fit in top left corner"
            )

            image[(0, 0)] = rotated_tile
            image_tile_nums[(0, 0)] = start_corner_num
            break
    else:
        raise ValueError("couldn't fit corner 1 into top-left position")

    # Now we march on from this tile right-ward to fill the next 11 tiles, then
    # move down a row, repeat the right-ward march, until we have assembled the full image
    for y in range(12):
        for x in range(12):
            if x == y == 0:
                continue  # (0,0) was done above

            this_pos = x, y
            if x == 0:
                # When we are at the first tile in a row (the left most one /
                # first column), then the previous tile we want to match is the
                # one above it.
                prev_pos = x, y - 1
            else:
                # Otherwise we are matching the tile to the left.
                prev_pos = x - 1, y
            print(f"at position {this_pos}, previous position was {prev_pos}")

            prev_tile_num = image_tile_nums[prev_pos]
            prev_tile = image[prev_pos]

            # Similar to the block above, when we are past the first column, we
            # will match the right border of the previous tile to the left
            # border of this tile. When we are at the first column, we compare
            # the bottom border of whats above to the top border of this tile.
            #
            # This could be more sophisticated and make sure that we are
            # matching both above and to the left (when past the first
            # column/row), but in the problem's input this is fine - there is
            # only one tile that matches at each iteration.
            if x > 0:
                border_to_match = right_border(prev_tile)
                border_fn = left_border
                # for logging
                prev_border_side, this_border_side = "right", "left"
            else:
                border_to_match = bottom_border(prev_tile)
                border_fn = top_border
                prev_border_side, this_border_side = "bottom", "top"

            # Which tile has a border matching the previous tile? Check the dict
            # containing the set of tile nums with this border, and remove the tile
            # num we've already placed
            s = border_to_tile[border_to_match] - {prev_tile_num}
            # Make sure there is only one in the set - we didn't build an
            # algorithm that can handle more than one candidate.
            if len(s) != 1:
                raise ValueError(
                    f"error trying to find tile to place next to {prev_tile_num} at {prev_pos} in this_pos={this_pos}:"
                    f' tiles that match border="{border_to_match}": {border_to_tile[border_to_match]}'
                )

            next_tile_num = s.pop()
            # print(f"from tile {prev_tile_num}, right connection is: {next_tile_num}")

            # We know which tile has the matching border, but we have to figure
            # out how to rotate/orient it so that the sides match up.
            for candidate in transformations(tiles[next_tile_num]):
                if border_fn(candidate) == border_to_match:
                    print(
                        f"tile {prev_tile_num}'s {prev_border_side} border ({border_to_match}) matches "
                        f"{this_border_side} border of {next_tile_num} ({left_border(candidate)}) after rotating/flipping"
                    )
                    image[this_pos] = candidate
                    image_tile_nums[this_pos] = next_tile_num
                    break
            else:
                raise ValueError(
                    f"couldn't rotate/flip tile {next_tile_num} to make it fit"
                )

        # print(f"done with row, image so far is: {image_tile_nums}")

    assert_image_valid(image)
    print("image looks valid, all borders match!")

    return image, image_tile_nums


def remove_borders(tile: Tile) -> Tile:
    return [t[1:-1] for t in tile[1:-1]]


def combine_tiles(image: Image) -> Tile:
    max_x, max_y = max(image.keys())
    rows_per_tile = len(image[0, 0])
    t = []
    for y in range(max_y + 1):
        for row_num in range(rows_per_tile):
            t.append("".join(image[x, y][row_num] for x in range(max_x + 1)))
    return t


# sea monster:
# ----------------------
# |                  # |
# |#    ##    ##    ###|
# | #  #  #  #  #  #   |
# ----------------------
#
# When looking for this pattern in the image, the spaces can be anything; only
# the # need to match. Also, you might need to rotate or flip your image before
# it's oriented correctly to find sea monsters.
monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


def indexes_of_char(ch, s):
    return [ix for ix, c in enumerate(s) if c == ch]


monster_positions = list(map(lambda row: indexes_of_char("#", row), monster))


def count_sea_monsters(tile: Tile) -> int:
    monster_rows = len(monster)
    monster_cols = len(monster[0])

    tile_rows = len(tile)
    tile_cols = len(tile[0])

    c = 0

    # if the tile has 96 rows, range from 0 to 93 so we can overlay the 3 rows
    # of the monster onto it (with the last group being rows [93,94,95]).
    for y in range(0, tile_rows - monster_rows + 1):
        for x in range(0, tile_cols - monster_cols + 1):

            # using (x, y) as an anchor point, we see if the monster could exist
            # from this anchor point. Do this by checking if the positions from
            # here contain the required '#' characters.
            if all(
                tile[y + j][x + i] == "#"
                for j, indices in enumerate(monster_positions)
                for i in indices
            ):
                c += 1

    return c


def count_roughness(tile: Tile, num_monsters: int) -> int:
    total_hashes = sum(row.count("#") for row in tile)
    hashes_in_monster = sum(row.count("#") for row in monster)
    return total_hashes - num_monsters * hashes_in_monster


def part2(inp: str) -> int:
    tiles = parse_input(inp)

    # this was the output of part1
    corner_tile_nums = {3343, 3821, 3677, 3709}

    image, image_tile_nums = assemble_image(tiles, corner_tile_nums)

    # TODO: remove all four borders from each tile, and make a new image out of
    # the results. Represent this as just a Tile since it is a List[str] rather
    # than the Image type which is a Dict of Tiles.
    #
    # then search for sea monsters - trying all 8 transformations of the mega
    # Tile. From the instructions, it seems like only one should contain >= 1
    # sea monster.
    #
    # Determine how rough the waters are in the sea monsters' habitat by
    # counting the number of # that are not part of a sea monster.

    image = {p: remove_borders(t) for p, t in image.items()}
    mega_tile = combine_tiles(image)
    print("\n".join(mega_tile))

    for t in transformations(mega_tile):
        num_monsters = count_sea_monsters(t)
        if num_monsters > 0:
            print(f"{num_monsters} sea monsters found")
            return count_roughness(t, num_monsters)

    raise ValueError("didn't find any sea monsters?")
