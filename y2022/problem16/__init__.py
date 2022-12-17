from typing import *
import re

# Valve LD has flow rate=0; tunnels lead to valves CL, QU
# the input varies between tunnel/tunnels, lead/leads, and valve/valves
input_pattern = re.compile(
    r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]+)"
)


def part1(inp: str):

    flow_rate = {}
    open_valves: set[str] = set()
    connections = {}

    for line in inp.split("\n"):
        m = re.fullmatch(input_pattern, line)
        assert m is not None, f"regex did not match line: {line}"
        valve = m.group(1)
        rate = int(m.group(2))
        flow_rate[valve] = rate

        connections[valve] = m.group(3).split(", ")

    # a naive approach would be to explore every permutation we could take
    #
    # or maybe ... from where we are, consider the tradeoff between opening a
    # valve which has a low flow rate or taking the time to move to another
    # cave/valve that has a higher flow rate (and paying the cost of the moves).
    # We should be able to know before we decide which one has more value in the
    # end - and go after that.
    # But to know what is best move to make we have to evaluate all options ...

    options: List[Dict[int, str]] = []

    def recurse(
        minutes_left: int,
        location: str,
        visited: Set[str],
        opened_valves: Set[str],
        opened_at: Dict[int, str],
    ):
        moved = False
        if minutes_left > 0:
            # see if we can open this valve
            if location not in opened_valves and flow_rate[location] > 0:
                new_dict = dict(opened_at)
                # if we open the valve now, it opens a minute from now
                new_dict[minutes_left - 1] = location
                recurse(
                    minutes_left - 1,
                    location,
                    visited,
                    opened_valves | {location},
                    new_dict,
                )
                moved = True
            # can we walk anywhere else
            # TODO: this shouldn't just be a blind walk, but picking a non-open valve to try to reach
            for new_location in connections[location]:
                # if new_location not in visited:
                recurse(
                    minutes_left - 1,
                    new_location,
                    visited | {new_location},
                    opened_valves,
                    opened_at,
                )
                moved = True

        # when there is nothing left to do (not just min)
        if not moved:
            options.append(opened_at)

    recurse(30, "AA", set(), set(), {})

    assert options, "no options stored?"

    # figure out which path had the most value
    def add_up_value(schedule: Dict[int, str]):
        return sum(
            minutes * flow_rate[location] for minutes, location in schedule.items()
        )

    return max(map(add_up_value, options))


def part2(inp: str):
    pass
