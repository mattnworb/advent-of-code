from . import find_sum_product

if __name__ == "__main__":
    with open("y2020/problem01/input") as f:
        inp = f.read(-1).strip()

    nums = [int(line) for line in inp.split("\n")]

    # part 1
    product = find_sum_product(nums, 2, 2020)
    if product:
        print("part 1:", product)
    else:
        print("part 1: no pairs found")

    # part 2
    product = find_sum_product(nums, 3, 2020)
    if product:
        print("part 2:", product)
    else:
        print("part 2: no triple found")
