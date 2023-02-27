from . import *
from collections import Counter
import pytest  # type: ignore


@pytest.fixture
def tiles():
    with open("y2020/problem20/input") as f:
        inp = f.read(-1).strip()

    return parse_input(inp)


def test_parse_input(tiles):
    assert len(tiles) == 144
    for tile in tiles.values():
        assert len(tile) == 10
        for line in tile:
            assert len(line) == 10

    assert tiles[1913] == [
        "##..#....#",
        ".#.#.#.###",
        "#...##.##.",
        ".....#.#.#",
        ".#......##",
        ".........#",
        "#...###..#",
        ".#..#.....",
        ".##...#..#",
        "#.#...#...",
    ]


def test_all_borders(tiles):
    b = list(all_borders(tiles[1913]))
    assert len(b) == 8
    assert set(b) == {
        "##..#....#",
        "#.#...#...",
        "#.#...#..#",
        "##.####.#.",
        "#....#..##",
        "...#...#.#",
        "#..#...#.#",
        ".#.####.##",
    }


def test_part1_example():
    with open("y2020/problem20/example_input") as f:
        example_input = f.read(-1).strip()
    assert part1(example_input) == 20899048083289


def test_rotate_right():
    tile = ["abc", "def", "ghi"]
    assert rotate_clockwise(tile) == ["gda", "heb", "ifc"]
    assert rotate_clockwise(tile, times=2) == ["ihg", "fed", "cba"]
    assert rotate_clockwise(tile, times=2) == ["ihg", "fed", "cba"]
    assert rotate_clockwise(tile, times=3) == ["cfi", "beh", "adg"]
    assert rotate_clockwise(tile, times=4) == tile


def test_flip_y():
    tile = ["abc", "def", "ghi"]
    assert flip_y(tile) == ["ghi", "def", "abc"]
    assert flip_y(flip_y(tile)) == tile


def test_flip_x():
    tile = ["abc", "def", "ghi"]
    assert flip_x(tile) == ["cba", "fed", "ihg"]
    assert flip_x(flip_x(tile)) == tile


def test_rotate_and_flip():
    tile = ["abc", "def", "ghi"]
    assert flip_y(flip_x(tile)) == rotate_clockwise(tile, times=2)


def test_transformations():
    # given a tile like:   ab
    #                      cd
    #
    # there are eight possible transformations:
    #
    # Simple rotations:
    #
    # ab  ca  dc  bd
    # cd  db  ba  ac
    #
    # and if we flip the original tile in either the x-axis or y-axis, there are
    # four new rotations possible:
    #
    # cd  ac  da  bd
    # ab  db  bc  ca

    tile = ["ab", "cd"]

    transforms = list(transformations(tile))
    assert len(transforms) == 8


def test_remove_borders():
    t = [
        "#...##.#..",
        "..#.#..#.#",
        ".###....#.",
        "###.##.##.",
        ".###.#####",
        ".##.#....#",
        "#...######",
        ".....#..##",
        "#.####...#",
        "#.##...##.",
    ]

    expected = [
        ".#.#..#.",
        "###....#",
        "##.##.##",
        "###.####",
        "##.#....",
        "...#####",
        "....#..#",
        ".####...",
    ]

    assert remove_borders(t) == expected


def test_combine_tiles():
    #  ab cd ef
    #  gh ij kl
    #
    #  mn op qr
    #  st uv wx
    #
    #  yz 12 34
    #  56 78 90

    image = {}
    image[0, 0] = ["ab", "gh"]
    image[1, 0] = ["cd", "ij"]
    image[2, 0] = ["ef", "kl"]

    image[0, 1] = ["mn", "st"]
    image[1, 1] = ["op", "uv"]
    image[2, 1] = ["qr", "wx"]

    image[0, 2] = ["yz", "56"]
    image[1, 2] = ["12", "78"]
    image[2, 2] = ["34", "90"]

    t = combine_tiles(image)

    assert t == ["abcdef", "ghijkl", "mnopqr", "stuvwx", "yz1234", "567890"]


tile_with_monsters = """
.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
""".strip().split(
    "\n"
)


def test_count_sea_monsters():
    c = Counter(count_sea_monsters(t) for t in transformations(tile_with_monsters))

    # only one transformation should have any sea monsters, and it should have two
    assert c == {0: 7, 2: 1}


def test_count_roughness():
    found = False
    for t in transformations(tile_with_monsters):
        num_monsters = count_sea_monsters(t)
        if num_monsters > 0:
            found = True
            assert count_roughness(t, num_monsters) == 273
            break
    assert found
