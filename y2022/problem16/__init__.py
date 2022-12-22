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
    flow_rate: Dict[str, int], connections: Dict[str, List[str]]
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

    # new_graph = {}
    # for v, conns in connections.items():
    #     if flow_rate[v] > 0:
    #         new_graph[v] = [k for k in dist[v] if flow_rate[k] > 0 and dist[v][k] > 0]

    # prune locations with flow_rate==0
    all_valves = set(flow_rate.keys())

    for v in all_valves:
        if flow_rate[v] == 0:
            del dist[v]
        else:
            for v2 in all_valves:
                if flow_rate[v2] == 0 or v == v2:
                    del dist[v][v2]

    return dist


def part1(inp: str, minutes: int = 30, start_location="AA"):

    flow_rate, connections = parse(inp)

    # create a new graph which has only non-zero-flow-rate valves as vertexes.
    # Compared with the original graph, the cost to travel from one node to
    # another will not always be 1. this gives us a smaller space of moves to
    # search.

    dist = compressed_graph(flow_rate, connections)

    @functools.cache
    def max_value(minutes_left: int, location: str, open_valves: frozenset[str]) -> int:
        # we don't need to know the path we take, just what the maximum value we can find from this position is
        options: List[Tuple[str, int]] = []

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
                (
                    "open " + location,
                    value
                    + max_value(
                        minutes_left - 1, location, frozenset(open_valves | {location})
                    ),
                )
            )

        # we can also try using this time to move to each connection
        # special case - starting at AA which has no flow
        if flow_rate[location] == 0:
            for new_location in connections[location]:
                if flow_rate[new_location] > 0:  # this seems wrong
                    options.append(
                        (
                            "move to " + new_location,
                            value
                            + max_value(minutes_left - 1, new_location, open_valves),
                        )
                    )
        else:
            for new_location, time_cost in dist[location].items():
                new_minutes_left = minutes_left - time_cost
                if new_minutes_left > 0:
                    options.append(
                        (
                            "move to " + new_location,
                            # `value` is just flow in one minute, if we are jumping ahead in time need to account for that
                            value * time_cost
                            + max_value(
                                minutes_left - time_cost, new_location, open_valves
                            ),
                        )
                    )

        return max(o[1] for o in options) if len(options) > 0 else 0

    return max_value(minutes, start_location, frozenset())


def part2(
    inp: str,
    minutes: int = 26,
):
    return 0
