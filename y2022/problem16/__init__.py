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


def compressed_graph(
    flow_rate: Dict[str, int],
    connections: Dict[str, List[str]],
    start_location: str,
) -> Dict[str, Dict[str, int]]:
    dist: Dict[str, Dict[str, int]] = {}
    for a in flow_rate:
        dist[a] = {}
        for b in flow_rate:
            dist[a][b] = 100000

    for v, conns in connections.items():
        for c in conns:
            dist[v][c] = 1

    for v in connections:
        dist[v][v] = 0

    for k in flow_rate:
        for i in flow_rate:
            for j in flow_rate:
                # if the distance from i to j is more than the distance from i
                # to j and j to k, update our estimate of the distance from i to
                # j
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # prune locations with flow_rate==0, except the starting point
    all_valves = set(flow_rate.keys())

    for v in all_valves:
        if v != start_location and flow_rate[v] == 0:
            del dist[v]
        else:
            for v2 in all_valves:
                if flow_rate[v2] == 0 or v == v2:
                    del dist[v][v2]

    return dist


def part1(inp: str, minutes: int = 30, start_location="AA"):

    flow_rate, connections = parse(inp)

    nonzero_flow_valves = set(v for v, amt in flow_rate.items() if amt > 0)

    # create a new graph which has only non-zero-flow-rate valves as vertexes.
    # Compared with the original graph, the cost to travel from one node to
    # another will not always be 1. this gives us a smaller space of moves to
    # search.

    dist = compressed_graph(flow_rate, connections, start_location)

    @functools.cache
    def max_value(
        minutes_left: int,
        location: str,
        open_valves: frozenset[str],
        # this is a function of open_valves, but we can avoid recalculating it each time
        value_so_far: int,
    ) -> int:
        # we don't need to know the path we take, just what the maximum value we can find from this position is
        max_option = 0

        if minutes_left <= 1:
            return value_so_far

        # if everything with non-zero flow rate is open, no moves to make, just count the value and tick the clock down
        if open_valves == nonzero_flow_valves:
            return value_so_far + max_value(
                minutes_left - 1,
                location,
                open_valves,
                value_so_far,
            )

        if location not in open_valves and flow_rate[location] > 0:
            # we can try to open this valve ... it doesn't open this minute but in the next one
            max_option = max(
                max_option,
                value_so_far
                + max_value(
                    minutes_left - 1,
                    location,
                    frozenset(open_valves | {location}),
                    value_so_far + flow_rate[location],
                ),
            )

        # we can also try using this time to move to each connection
        # special case - starting at AA which has no flow
        if flow_rate[location] == 0:
            for new_location in connections[location]:
                max_option = max(
                    max_option,
                    value_so_far
                    + max_value(
                        minutes_left - 1,
                        new_location,
                        open_valves,
                        value_so_far,
                    ),
                )
        else:
            for new_location, time_cost in dist[location].items():
                new_minutes_left = minutes_left - time_cost
                if new_minutes_left > 0:
                    max_option = max(
                        max_option,
                        # `value_so_far` is just flow in one minute, if we are jumping ahead in time need to account for that
                        value_so_far * time_cost
                        + max_value(
                            minutes_left - time_cost,
                            new_location,
                            open_valves,
                            value_so_far,
                        ),
                    )

        return max_option

    return max_value(minutes, start_location, frozenset(), 0)


def part2(
    inp: str,
    minutes: int = 26,
    start_location="AA",
):

    flow_rate, connections = parse(inp)

    nonzero_flow_valves = set(v for v, amt in flow_rate.items() if amt > 0)

    # create a new graph which has only non-zero-flow-rate valves as vertexes.
    # Compared with the original graph, the cost to travel from one node to
    # another will not always be 1. this gives us a smaller space of moves to
    # search.

    dist = compressed_graph(flow_rate, connections, start_location)

    @functools.cache
    def max_value(
        minutes_left: int,
        location: str,
        valves_to_close: frozenset[str],
        # this is a function of open_valves, but we can avoid recalculating it each time
        value_so_far: int,
    ) -> int:
        # we don't need to know the path we take, just what the maximum value we can find from this position is
        max_option = 0

        if minutes_left <= 1:
            return value_so_far

        # if everything with non-zero flow rate is open, no moves to make, just count the value and tick the clock down
        if len(valves_to_close) == 0:
            return value_so_far + max_value(
                minutes_left - 1,
                location,
                valves_to_close,
                value_so_far,
            )

        if location in valves_to_close and flow_rate[location] > 0:
            # we can try to open this valve ... it doesn't open this minute but in the next one
            max_option = max(
                max_option,
                value_so_far
                + max_value(
                    minutes_left - 1,
                    location,
                    frozenset(valves_to_close - {location}),
                    value_so_far + flow_rate[location],
                ),
            )

        # we can also try using this time to move to each connection
        # special case - starting at AA which has no flow
        if flow_rate[location] == 0:
            for new_location in connections[location]:
                max_option = max(
                    max_option,
                    value_so_far
                    + max_value(
                        minutes_left - 1,
                        new_location,
                        valves_to_close,
                        value_so_far,
                    ),
                )
        else:
            for new_location, time_cost in dist[location].items():
                new_minutes_left = minutes_left - time_cost
                if new_minutes_left > 0:
                    max_option = max(
                        max_option,
                        # `value_so_far` is just flow in one minute, if we are jumping ahead in time need to account for that
                        value_so_far * time_cost
                        + max_value(
                            minutes_left - time_cost,
                            new_location,
                            valves_to_close,
                            value_so_far,
                        ),
                    )

        return max_option

    # split the valves into two sets: one for me to close each of, and one for the elephant
    # figure out which option has the max value

    combined_max = 0
    valves = list(nonzero_flow_valves)
    for i in range(0, 2 ** len(nonzero_flow_valves)):
        me_close = set()
        # test which bits are set in i
        for n in range(len(nonzero_flow_valves)):
            if i & (1 << n) != 0:
                me_close.add(valves[n])

        elephant_close = frozenset(nonzero_flow_valves - me_close)
        combined_max = max(
            combined_max,
            max_value(minutes, start_location, frozenset(me_close), 0)
            + max_value(minutes, start_location, elephant_close, 0),
        )
        print(f"i={i}, max is {combined_max}")

    return max_value(minutes, start_location, frozenset(), 0)
