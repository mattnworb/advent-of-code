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
    # print(f"map is length ({len(seatmap)},{len(seatmap[0])})")
    positions = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
    for p in positions:
        # skip (0,0)
        if p[0] == 0 and p[1] == 0:
            continue
        a = r + p[0]
        b = c + p[1]
        if a < 0 or b < 0 or a >= len(seatmap) or b >= len(seatmap[a]):
            continue
        # print(f"testing ({a},{b})")
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


def count_visible_occupied(seatmap: List[str], r: int, c: int, debug=False) -> int:
    count = 0

    max_r = len(seatmap)
    max_c = len(seatmap[0])

    if r >= max_r or c >= max_c or r < 0 or c < 0:
        raise ValueError("input seat is out of bounds")

    def log(msg):
        if debug:
            print(msg)

    # 8 cardinal directions
    log("\n".join(seatmap))
    log(f"checking directions starting from ({r},{c})")
    # north
    for x in range(r - 1, -1, -1):
        log(f"north: ({x},{c})")
        if seatmap[x][c] == occupied_seat:
            log("found occupied seat")
            count += 1
        if seatmap[x][c] != ".":
            log("north: saw seat, stopping")
            break

    # # south
    for x in range(r + 1, max_r):
        log(f"south: ({x},{c})")
        if seatmap[x][c] == occupied_seat:
            log("found occupied seat")
            count += 1
        if seatmap[x][c] != ".":
            log("south: saw seat, stopping")
            break

    # west
    for y in range(c - 1, -1, -1):
        log(f"west: ({r},{y})")
        if seatmap[r][y] == occupied_seat:
            log("found occupied seat")
            count += 1
        if seatmap[r][y] != ".":
            log("west: saw seat, stopping")
            break
    # east
    for y in range(c + 1, max_c):
        log(f"east: ({r},{y})")
        if seatmap[r][y] == occupied_seat:
            log("found occupied seat")
            count += 1
        if seatmap[r][y] != ".":
            log("east: saw seat, stopping")
            break

    # northwest
    # for d in range(1, min(r, c) + 1):
    #     if seatmap[r - d][c - d] == occupied_seat:
    #         count += 1

    # # southeast
    # for d in range(1, max(r, c) + 1):
    #     if seatmap[r + d][c + d] == occupied_seat:
    #         count += 1

    # northwest
    # southeast

    # diagonals
    s1, s2, s3, s4 = False, False, False, False
    for d in range(1, max(max_r, max_c)):
        if not s1 and r + d < max_r and c + d < max_c:
            log(f"southeast: checking ({r+d}, {c+d})")
            if seatmap[r + d][c + d] == occupied_seat:
                log("found occupied seat")
                count += 1
            if seatmap[r + d][c + d] != ".":
                log(f"southeast: stopping")
                s1 = True
        if not s2 and r + d < max_r and c - d >= 0:
            log(f"southwest: checking ({r+d}, {c-d}): {seatmap[r + d][c - d]}")
            if seatmap[r + d][c - d] == occupied_seat:
                log("found occupied seat")
                count += 1
            if seatmap[r + d][c - d] != ".":
                log(f"southwest: stopping")
                s2 = True
        if not s3 and r - d >= 0 and c + d < max_c:
            log(f"northeast: checking ({r-d}, {c+d})")
            if seatmap[r - d][c + d] == occupied_seat:
                log("found occupied seat")
                count += 1
            if seatmap[r - d][c + d] != ".":
                log(f"northeast: stopping")
                s3 = True
        if not s4 and r - d >= 0 and c - d >= 0:
            log(f"northwest: checking ({r-d}, {c-d})")
            if seatmap[r - d][c - d] == occupied_seat:
                log("found occupied seat")
                count += 1
            if seatmap[r - d][c - d] != ".":
                log(f"northwest: stopping")
                s4 = True

    return count
