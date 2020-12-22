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