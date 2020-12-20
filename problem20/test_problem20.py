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


def test_borders(tiles):
    b = borders(tiles[1913])
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
    pass
