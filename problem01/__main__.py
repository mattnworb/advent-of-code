from problem01 import find_pair

if __name__ == "__main__":
    with open("problem01/input") as f:
        inp = f.read(-1).strip()

    nums = [int(line) for line in inp.split("\n")]

    pair = find_pair(nums, 2020)
    if pair:
        a, b = pair
        print(a * b)
    else:
        print("no pairs found")
