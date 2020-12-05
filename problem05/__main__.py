from problem05 import *

if __name__ == "__main__":
    with open("problem05/input") as f:
        inp = f.read(-1).strip()

    seats = inp.split("\n")
    highest = max(seat_id(decode_seat(seat)) for seat in seats)
    print("part 1:", highest)

    print("part 2:", "TODO")
