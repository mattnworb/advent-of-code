from problem20 import *

import pytest  # type: ignore


@pytest.fixture
def tiles():
    with open("problem20/input") as f:
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


def test_borders(tiles):
    b = borders(tiles[1913])
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
    with open("problem20/example_input") as f:
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
