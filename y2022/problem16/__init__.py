from typing import *
import re
import functools

# input is like "Valve LD has flow rate=0; tunnels lead to valves CL, QU"
# the input varies between tunnel/tunnels, lead/leads, and valve/valves
input_pattern = re.compile(
    r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]+)"
)


def parse(inp: str) -> Tuple[Dict[str, int], Dict[str, List[str]]]:
    """Parse the input into two dicts: the flow rate for each valve, and a list of connections from one valve to another"""
    flow_rate = {}
    connections = {}

    for line in inp.split("\n"):
        m = re.fullmatch(input_pattern, line)
        assert m is not None, f"regex did not match line: {line}"
        valve = m.group(1)
        rate = int(m.group(2))
        flow_rate[valve] = rate

        connections[valve] = m.group(3).split(", ")
    return flow_rate, connections


def part1(inp: str, minutes: int = 30, start_location="AA"):

    flow_rate, connections = parse(inp)

    @functools.cache
    def max_value(minutes_left: int, location: str, open_valves: frozenset[str]) -> int:
        # we don't need to know the path we take, just what the maximum value we can find from this position is
        options = []

        # everything already open flows one tick
        value = sum(flow_rate[valve] for valve in open_valves)

        if minutes_left <= 1:
            return value

        # if everything with non-zero flow rate is open, no moves to make, just count the value and tick the clock down
        if open_valves == set(v for v, amt in flow_rate.items() if amt > 0):
            return value + max_value(minutes_left - 1, location, open_valves)

        if location not in open_valves and flow_rate[location] > 0:
            # we can try to open this valve ... it doesn't open this minute but in the next one
            options.append(
                value
                + max_value(
                    minutes_left - 1, location, frozenset(open_valves | {location})
                )
            )

        # we can also try using this time to move to each connection
        for new_location in connections[location]:
            options.append(
                value + max_value(minutes_left - 1, new_location, open_valves)
            )

        return max(options)

    return max_value(minutes, start_location, frozenset())


def part2(inp: str):
    pass
