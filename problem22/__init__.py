from typing import *

# import math

# It only takes a few hours of sailing the ocean on a raft for boredom to sink
# in. Fortunately, you brought a small deck of space cards! You'd like to play a
# game of Combat, and there's even an opponent available: a small crab that
# climbed aboard your raft before you left.
#
# Fortunately, it doesn't take long to teach the crab the rules.
#
# Before the game starts, split the cards so each player has their own deck
# (your puzzle input). Then, the game consists of a series of rounds: both
# players draw their top card, and the player with the higher-valued card wins
# the round. The winner keeps both cards, placing them on the bottom of their
# own deck so that the winner's card is above the other card. If this causes a
# player to have all of the cards, they win, and the game ends.
Deck = List[int]


def log(s: str):
    # print(s)
    pass


def part1(inp: str):
    deck1, deck2 = parse_input(inp)
    deck1, deck2 = play_game(deck1, deck2)

    # who won?
    winning_deck = deck1 if len(deck1) > 0 else deck2
    return score(winning_deck)


def parse_input(inp: str) -> Tuple[Deck, Deck]:
    parts = inp.split("\n\n")
    assert len(parts) == 2

    p1 = parts[0].split("\n")
    assert p1[0].startswith("Player 1:")

    p2 = parts[1].split("\n")
    assert p2[0].startswith("Player 2:")

    return list(map(int, p1[1:])), list(map(int, p2[1:]))


def play_game(deck1: Deck, deck2: Deck, max_rounds: int = None) -> Tuple[Deck, Deck]:
    deck1 = list(deck1)
    deck2 = list(deck2)

    round_num = 1
    while (
        len(deck1) > 0
        and len(deck2) > 0
        and (max_rounds is None or round_num < max_rounds)
    ):
        log(f"-- Round {round_num} --")
        log(f"Player 1's deck: {deck1}")
        log(f"Player 2's deck: {deck2}")

        c1, c2 = deck1.pop(0), deck2.pop(0)

        log(f"Player 1 plays: {c1}")
        log(f"Player 2 plays: {c2}")

        if round_num % 1000 == 0:
            print(
                f"Round {round_num}: player 1 has {len(deck1)} cards, player 2 has {len(deck2)}"
            )

        if c1 > c2:
            log("Player 1 wins the round!")
            # player 1 wins
            # winning card goes first
            deck1.append(c1)
            deck1.append(c2)
        elif c2 > c1:
            log("Player 2 wins the round!")
            # winning card goes first
            deck2.append(c2)
            deck2.append(c1)
        else:
            raise ValueError("ties shouldn't happen")

        round_num += 1

    assert len(deck1) == 0 or len(deck2) == 0
    print(f"Game done after {round_num} rounds")

    return deck1, deck2


def score(winning_deck: Deck) -> int:
    num_cards = len(winning_deck)
    return sum((num_cards - ix) * card for ix, card in enumerate(winning_deck))
