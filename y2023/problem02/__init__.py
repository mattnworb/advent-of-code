from typing import *


# The Elf would first like to know which games would have been possible if the
# bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#
# ...
#
# Determine which games would have been possible if the bag had been loaded with
# only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the
# IDs of those games?
def part1(inp: str):
    max_red = 12
    max_green = 13
    max_blue = 14

    valid_games = []

    for line in inp.split("\n"):
        g, text = line.split(": ")
        game_id = int(g[len("Game ") :])

        game_is_valid = True

        for draw in text.split("; "):
            red, green, blue = 0, 0, 0
            for s in draw.split(", "):
                n, color = s.split(" ")
                num = int(n)
                if color == "green":
                    green = num
                elif color == "blue":
                    blue = num
                elif color == "red":
                    red = num
                else:
                    raise ValueError(f"unexpected color {color}")

            if green > max_green or red > max_red or blue > max_blue:
                game_is_valid = False

        if game_is_valid:
            valid_games.append(game_id)

    return sum(valid_games)


def part2(inp: str):
    pass
