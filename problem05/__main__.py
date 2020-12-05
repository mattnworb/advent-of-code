from problem05 import *

if __name__ == "__main__":
    with open("problem05/input") as f:
        inp = f.read(-1).strip()

    seats = inp.split("\n")
    highest = max(seat_id(decode_seat(seat)) for seat in seats)
    print("part 1:", highest)

    all_seat_ids = sorted(seat_id(decode_seat(seat)) for seat in seats)
    for i in range(len(all_seat_ids)):
        if all_seat_ids[i + 1] != all_seat_ids[i] + 1:
            my_id = all_seat_ids[i] + 1
            break

    assert my_id not in all_seat_ids

    print("part 2:", my_id)
