from problem02 import count_valid_passwords

if __name__ == "__main__":
    with open("problem02/input") as f:
        inp = f.read(-1).strip()

    lines = inp.split("\n")

    # part 1
    print("part 1:", count_valid_passwords(lines))
