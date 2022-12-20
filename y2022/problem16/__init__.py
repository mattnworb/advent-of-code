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

    # create a new graph which has only non-zero-flow-rate valves as vertexes.
    # Compared with the original graph, the cost to travel from one node to
    # another will not always be 1. this gives us a smaller space of moves to
    # search.

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

    new_graph = {}
    for v, conns in connections.items():
        if flow_rate[v] > 0:
            new_graph[v] = [k for k in dist[v] if flow_rate[k] > 0 and dist[v][k] > 0]
            print(f"original: {v} -> {conns}")
            print(
                f"new:      {v} -> {new_graph[v]}, weights={[dist[v][k] for k in new_graph[v]]}"
            )

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
        # special case - starting at AA which has no flow
        if flow_rate[location] == 0:
            for new_location in connections[location]:
                options.append(
                    value + max_value(minutes_left - 1, new_location, open_valves)
                )
        else:
            for new_location in new_graph[location]:
                weight = dist[location][new_location]
                if minutes_left - weight > 1:
                    options.append(
                        value
                        + max_value(minutes_left - weight, new_location, open_valves)
                    )

        return max(options) if len(options) > 0 else 0

    return max_value(minutes, start_location, frozenset())
    # return 0


def part2(
    inp: str,
    minutes: int = 26,
):
    flow_rate, connections = parse(inp)

    # TODO: does the use of two location parameters like this mess up the
    # caching? given the same time and open_valves, the max answer is the same
    # if you swap the player's positions

    @functools.cache
    def max_value(
        minutes_left: int, location1: str, location2: str, open_valves: frozenset[str]
    ) -> int:

        # log_ctr = (log_ctr + 1) % 1000
        # if log_ctr == 0:
        # print(
        #     f"max_value(minutes_left={minutes_left}, location1={location1}, location2={location2}, open_valves={open_valves}"
        # )

        # we don't need to know the path we take, just what the maximum value we can find from this position is
        options = []

        # everything already open flows one tick
        value = sum(flow_rate[valve] for valve in open_valves)

        if minutes_left <= 1:
            return value

        # if everything with non-zero flow rate is open, no moves to make, just count the value and tick the clock down
        if open_valves == set(v for v, amt in flow_rate.items() if amt > 0):
            return value + max_value(
                minutes_left - 1, location1, location2, open_valves
            )

        # options for part 2:
        # 1. both players move
        # 2. A opens, B moves
        # 3. A moves, B opens
        # 4. both players open

        # 1. both players move
        can_open1 = location1 not in open_valves and flow_rate[location1] > 0
        can_open2 = location2 not in open_valves and flow_rate[location2] > 0

        if can_open1 and can_open2:
            options.append(
                value
                + max_value(
                    minutes_left - 1,
                    location1,
                    location2,
                    frozenset(open_valves | {location1, location2}),
                )
            )

        # 2. A opens, B moves
        if can_open1:  # can_open2 doesn't matter (I think?)
            # add each permutation of open valve 1 + other player moves
            for new_location2 in connections[location2]:
                a, b = sorted([location1, new_location2])
                options.append(
                    value
                    + max_value(
                        minutes_left - 1,
                        a,
                        b,
                        frozenset(open_valves | {location1}),
                    )
                )

        # 3. A moves, B opens
        if can_open2:
            # add each permutation of open valve 2 +  player1  moves
            for new_location1 in connections[location1]:
                a, b = sorted([new_location1, location2])
                options.append(
                    value
                    + max_value(
                        minutes_left - 1,
                        a,
                        b,
                        frozenset(open_valves | {location2}),
                    )
                )

        # and 4. each permutation of both players moving
        for new_location1 in connections[location1]:
            for new_location2 in connections[location2]:
                a, b = sorted([new_location1, new_location2])
                options.append(value + max_value(minutes_left - 1, a, b, open_valves))

        return max(options)

    return max_value(minutes, "AA", "AA", frozenset())
