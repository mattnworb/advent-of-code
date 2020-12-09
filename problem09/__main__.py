from problem09 import *

if __name__ == "__main__":
    with open("problem09/input") as f:
        inp = f.read(-1).strip()

    # The first step of attacking the weakness in the XMAS data is to find the
    # first number in the list (after the preamble) which is not the sum of two
    # of the 25 numbers before it. What is the first number that does not have
    # this property?

    nums = [int(line) for line in inp.split("\n")]

    first_invalid = find_not_sum_pair(nums)
    print("part 1:", first_invalid)

    window = find_contiguous_sum(nums, first_invalid)
    output = min(window) + max(window)
    print("part 2:", output)
    print(f"(window size was {len(window)})")
