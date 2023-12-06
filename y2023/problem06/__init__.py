from typing import *
from functools import reduce


# example input
# Time:      7  15   30
# Distance:  9  40  200
def part1(inp: str):
    lines = inp.split("\n")
    times = [int(s) for s in lines[0].split()[1:]]
    distances = [int(s) for s in lines[1].split()[1:]]

    assert len(times) == len(distances)

    # Your toy boat has a starting speed of zero millimeters per millisecond.
    # For each whole millisecond you spend at the beginning of the race holding
    # down the button, the boat's speed increases by one millimeter per
    # millisecond.

    # distance traveled can be calculated with the following formula:
    #
    # distance = (time_available - time_button_held) * time_button_held
    #
    # examples:
    #
    # """
    # So, because the first race lasts 7 milliseconds, you only have a few
    # options:
    # - Don't hold the button at all (that is, hold it for 0 milliseconds) at
    #   the start of the race. The boat won't move; it will have traveled 0
    #   millimeters by the end of the race.
    # - Hold the button for 1 millisecond at the start of the race. Then, the
    #   boat will travel at a speed of 1 millimeter per millisecond for 6
    #   milliseconds, reaching a total distance traveled of 6 millimeters.
    # - Hold the button for 2 milliseconds, giving the boat a speed of 2
    #   millimeters per millisecond. It will then get 5 milliseconds to move,
    #   reaching a total distance of 10 millimeters.
    # """

    winning_options = []
    for race_num in range(len(times)):
        # no point in calculating time_button_held=0 or
        # time_button_held=time_available as the result will be distance=0
        # always
        time_available = times[race_num]
        winners = 0
        for time_button_held in range(1, time_available):
            distance = (time_available - time_button_held) * time_button_held
            if distance > distances[race_num]:
                winners += 1
        winning_options.append(winners)

    return reduce(lambda a, b: a * b, winning_options)


def part2(inp: str):
    pass
