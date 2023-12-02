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


# As you continue your walk, the Elf poses a second question: in each game you
# played, what is the fewest number of cubes of each color that could have been
# in the bag to make the game possible?
#
# ...
#
# The power of a set of cubes is equal to the numbers of red, green, and blue
# cubes multiplied together. The power of the minimum set of cubes in game 1 is
# 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these
# five powers produces the sum 2286.
#
# For each game, find the minimum set of cubes that must have been present. What
# is the sum of the power of these sets?


def part2(inp: str):
    total_power = 0

    for line in inp.split("\n"):
        # new game:
        _, text = line.split(": ")
        min_red, min_blue, min_green = 0, 0, 0

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

            min_red = max(red, min_red)
            min_green = max(green, min_green)
            min_blue = max(blue, min_blue)

        # draws are done
        total_power += min_red * min_green * min_blue
    return total_power
