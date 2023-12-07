from typing import *

# To play Camel Cards, you are given a list of hands and their corresponding bid
# (your puzzle input). For example:

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
#
# This example shows five hands; each hand is followed by its bid amount. Each
# hand wins an amount equal to its bid multiplied by its rank, where the weakest
# hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the
# strongest hand. Because there are five hands in this example, the strongest
# hand will have rank 5 and its bid will be multiplied by 5.
#
# -----
#
# My first instinct is to store the input in a dict of hand to bid, sort the keys using a custom compartor, then iterate thru
#
# but are there duplicate hands? ... not in my input

from enum import Enum
from collections import Counter
from functools import cmp_to_key


class HandType(Enum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7


def part1(inp: str):
    def hand_type(hand: str):
        assert len(hand) == 5
        c = Counter(hand)
        freq_by_label = c.most_common()

        if freq_by_label[0][1] == 5:
            return HandType.FIVE_OF_A_KIND

        if freq_by_label[0][1] == 4:
            return HandType.FOUR_OF_A_KIND

        if freq_by_label[0][1] == 3 and freq_by_label[1][1] == 2:
            return HandType.FULL_HOUSE

        if freq_by_label[0][1] == 3:
            return HandType.THREE_OF_A_KIND

        if freq_by_label[0][1] == 2 and freq_by_label[1][1] == 2:
            return HandType.TWO_PAIR

        if freq_by_label[0][1] == 2 and freq_by_label[1][1] == 1:
            return HandType.ONE_PAIR

        if freq_by_label[0][1] == 1:
            return HandType.HIGH_CARD

        raise ValueError("couldn't determine hand type of " + hand)

    CARD_ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def hand_sort(a: str, b: str) -> int:
        # cmp signature is: A comparison function is any callable that accepts two
        # arguments, compares them, and returns a negative number for less-than,
        # zero for equality, or a positive number for greater-than
        assert len(a) == len(b) == 5

        # same hand
        if a == b:
            return 0

        type_a, type_b = hand_type(a), hand_type(b)

        # lower enum cardinal value == higher ranking
        if type_a.value < type_b.value:
            return 1

        if type_a.value > type_b.value:
            return -1

        # same type, figure out which card starting from the left is higher-ranked
        assert type_a == type_b

        for card_a, card_b in zip(a, b):
            if card_a == card_b:
                continue

            ia, ib = CARD_ORDER.index(card_a), CARD_ORDER.index(card_b)

            return 1 if ia < ib else -1

        raise ValueError(f"shouldn't have gotten here, hands: {(a,b)}")

    hands_to_bids = {}
    for line in inp.split("\n"):
        hand, bid = line.split()
        hands_to_bids[hand] = int(bid)

    total_winnings = 0
    for ix, hand in enumerate(sorted(hands_to_bids, key=cmp_to_key(hand_sort))):
        rank = ix + 1
        total_winnings += rank * hands_to_bids[hand]

    return total_winnings


# Probably simpler to just duplicate code here and slightly alter the functions rather than make them work for both parts
def part2(inp: str):
    def hand_type(hand: str):
        assert len(hand) == 5
        c = Counter(hand)
        freq_by_label = c.most_common()

        # different from part1 - "J" is joker/wildcard and we have to factor it
        # in In the case where there are more than one J, I *think* it is always
        # the best move to add them to whatever card in the hand has the highest
        # frequency. For example if there are two Js, to make ONE_PAIR into
        # FOUR_OF_A_KIND, THREE_OF_A_KIND into FIVE_OF_A_KIND, etc. 3 Js should
        # turn ONE_PAIR to FIVE_OF_A_KIND, or HIGH_CARD into FOUR_OF_A_KIND.

        num_jokers = c["J"]

        # instead of looking at highest freq card, find highest non-joker card

        if num_jokers == 5:
            highest_freq = num_jokers
        elif freq_by_label[0][0] == "J":
            highest_freq = freq_by_label[1][1] + num_jokers
        else:
            highest_freq = freq_by_label[0][1] + num_jokers

        if highest_freq == 5:
            return HandType.FIVE_OF_A_KIND

        if highest_freq == 4:
            return HandType.FOUR_OF_A_KIND

        if highest_freq == 3 and freq_by_label[1][1] == 2:
            return HandType.FULL_HOUSE

        if highest_freq == 3:
            return HandType.THREE_OF_A_KIND

        if highest_freq == 2 and freq_by_label[1][1] == 2:
            return HandType.TWO_PAIR

        if highest_freq == 2 and freq_by_label[1][1] == 1:
            return HandType.ONE_PAIR

        if highest_freq == 1:
            return HandType.HIGH_CARD

        raise ValueError("couldn't determine hand type of " + hand)

    CARD_ORDER = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    def hand_sort(a: str, b: str) -> int:
        # cmp signature is: A comparison function is any callable that accepts two
        # arguments, compares them, and returns a negative number for less-than,
        # zero for equality, or a positive number for greater-than
        assert len(a) == len(b) == 5

        # same hand
        if a == b:
            return 0

        type_a, type_b = hand_type(a), hand_type(b)

        # lower enum cardinal value == higher ranking
        if type_a.value < type_b.value:
            return 1

        if type_a.value > type_b.value:
            return -1

        # same type, figure out which card starting from the left is higher-ranked
        assert type_a == type_b

        for card_a, card_b in zip(a, b):
            if card_a == card_b:
                continue

            ia, ib = CARD_ORDER.index(card_a), CARD_ORDER.index(card_b)

            return 1 if ia < ib else -1

        raise ValueError(f"shouldn't have gotten here, hands: {(a,b)}")

    hands_to_bids = {}
    for line in inp.split("\n"):
        hand, bid = line.split()
        hands_to_bids[hand] = int(bid)

    total_winnings = 0
    ranked_hands = sorted(hands_to_bids, key=cmp_to_key(hand_sort))
    for ix, hand in enumerate(ranked_hands):
        rank = ix + 1
        total_winnings += rank * hands_to_bids[hand]

    return total_winnings
