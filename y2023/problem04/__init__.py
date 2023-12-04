from typing import *
from collections import Counter


def part1(inp: str):
    total = 0
    for line in inp.split("\n"):
        numbers = line.split(": ")[1]
        winning, have = numbers.split("| ")
        winners = {int(s) for s in winning.split()}
        mine = {int(s) for s in have.split()}
        num_winners = len(winners & mine)
        if num_winners > 0:
            total += 1 << (num_winners - 1)
    return total


def part2(inp: str):
    c: Counter[int] = Counter()
    for line in inp.split("\n"):
        card, numbers = line.split(": ")
        # "Card NN"
        card_num = int(card[5:])
        c[card_num] += 1
        winning, have = numbers.split("| ")
        winners = {int(s) for s in winning.split()}
        mine = {int(s) for s in have.split()}
        num_winners = len(winners & mine)

        # win one copy each of the cards after this one
        # so if score is 2, win one copy of cards N+1 and N+2
        # for x in range(c[card_num]):
        for n in range(num_winners):
            # don't add just 1, because we need to consider each copy of the
            # card too and the winners it generates (by the time we get to card
            # N in the input we have already figured out how many copies of it
            # we have won from previous cards)
            c[card_num + n + 1] += c[card_num]
    return sum(c.values())
