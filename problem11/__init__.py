from typing import List

occupied_seat = "#"
empty_seat = "L"


def solve_part1(inp: str) -> int:
    seats = inp.split("\n")

    rounds = 0
    prev_map = list(seats)  # copy
    while rounds < 1000:
        new_map: List[str] = []
        for r in range(len(seats)):
            new_row = ""
            for c in range(len(seats[r])):

                # The following rules are applied to every seat simultaneously:
                #
                # - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                # - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                # - Otherwise, the seat's state does not change.
                seat = prev_map[r][c]
                if seat == empty_seat and count_occupied(prev_map, r, c) == 0:
                    new_seat = occupied_seat
                elif seat == occupied_seat and count_occupied(prev_map, r, c) >= 4:
                    new_seat = empty_seat
                else:
                    new_seat = seat
                new_row += new_seat

            new_map.append(new_row)

        rounds += 1

        # print(f"Round {rounds}:")
        # print("\n".join(new_map), "\n")

        # check if done
        if new_map == prev_map:
            return sum(row.count(occupied_seat) for row in new_map)

        prev_map = new_map

    raise ValueError("too many rounds? 1000 and not stable")


def count_occupied(seatmap: List[str], r: int, c: int) -> int:
    count = 0

    # check adjacent squares, skip (0,0)
    for d in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
        a = r + d[0]
        b = c + d[1]
        if a < 0 or b < 0 or a >= len(seatmap) or b >= len(seatmap[a]):
            continue
        if seatmap[a][b] == occupied_seat:
            count += 1
    return count


# changes from part1:
#
# Now, instead of considering just the eight immediately adjacent seats,
# consider the first seat in each of those eight directions. For example, the
# empty seat below would see eight occupied seats...
#
# Also, people seem to be more tolerant than you expected: it now takes five or
# more visible occupied seats for an occupied seat to become empty (rather than
# four or more from the previous rules). The other rules still apply: empty
# seats that see no occupied seats become occupied, seats matching no rule don't
# change, and floor never changes.
def solve_part2(inp: str) -> int:
    seats = inp.split("\n")

    rounds = 0
    prev_map = list(seats)  # copy
    while rounds < 1000:

        # print(f"Round {rounds}:")
        # print("\n".join(prev_map), "\n")

        new_map: List[str] = []
        for r in range(len(seats)):
            new_row = ""
            for c in range(len(seats[r])):
                seat = prev_map[r][c]
                if seat == empty_seat and count_visible_occupied(prev_map, r, c) == 0:
                    new_seat = occupied_seat
                elif (
                    seat == occupied_seat
                    and count_visible_occupied(prev_map, r, c) >= 5
                ):
                    new_seat = empty_seat
                else:
                    new_seat = seat
                new_row += new_seat

            new_map.append(new_row)

        rounds += 1

        # check if done
        if new_map == prev_map:
            return sum(row.count(occupied_seat) for row in new_map)

        prev_map = new_map

    raise ValueError("too many rounds? 1000 and not stable")


def count_visible_occupied(seatmap: List[str], r: int, c: int) -> int:
    max_r = len(seatmap)
    max_c = len(seatmap[0])

    if r >= max_r or c >= max_c or r < 0 or c < 0:
        raise ValueError("input seat is out of bounds")

    count = 0

    # vectors
    for d in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
        # walk from the starting point until an edge or seeing a seat
        seen_seat = False
        x, y = r + d[0], c + d[1]
        while not seen_seat and x >= 0 and y >= 0 and x < max_r and y < max_c:
            if seatmap[x][y] == occupied_seat:
                count += 1
            if seatmap[x][y] != ".":
                seen_seat = True
            # TODO avoid needing to assign this twice
            x, y = x + d[0], y + d[1]

    return count
