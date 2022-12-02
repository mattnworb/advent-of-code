from typing import *

# Rock Paper Scissors is a game between two players. Each game contains many
# rounds; in each round, the players each simultaneously choose one of Rock,
# Paper, or Scissors using a hand shape. Then, a winner for that round is
# selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats
# Rock. If both players choose the same shape, the round instead ends in a draw.
#
# Appreciative of your help yesterday, one Elf gives you an encrypted strategy
# guide (your puzzle input) that they say will be sure to help you win. "The
# first column is what your opponent is going to play: A for Rock, B for Paper,
# and C for Scissors. The second column--" Suddenly, the Elf is called away to
# help with someone's tent.
#
# The second column, you reason, must be what you should play in response: X for
# Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious,
# so the responses must have been carefully chosen.
#
# The winner of the whole tournament is the player with the highest score. Your
# total score is the sum of your scores for each round. The score for a single
# round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3
# for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if
# the round was a draw, and 6 if you won).
#
# Since you can't be sure if the Elf is trying to help you or trick you, you
# should calculate the score you would get if you were to follow the strategy
# guide.
#
# ...
#
# What would your total score be if everything goes exactly according to your
# strategy guide?

move_scores = {
    # rock:
    "A": 1,
    "X": 1,
    # paper:
    "B": 2,
    "Y": 2,
    # scissor:
    "C": 3,
    "Z": 3,
}


def part1(inp: str):
    scores = []
    for line in inp.split("\n"):
        opponent, me = line.split(" ")
        if opponent not in ("A", "B", "C") or me not in ("X", "Y", "Z"):
            raise ValueError(f"bad parsing: {opponent} {me}")

        score = move_scores[me] + outcome_score(opponent, me)
        scores.append(score)
    return sum(scores)


def outcome_score(opponent: str, me: str) -> int:
    o = move_scores[opponent]
    m = move_scores[me]
    if o == m:
        return 3

    # opponent has rock
    if opponent == "A":
        return 0 if me == "Z" else 6
    # opponent has paper
    if opponent == "B":
        return 0 if me == "X" else 6
    # opponent has scissor
    else:
        return 0 if me == "Y" else 6


# The Elf finishes helping with the tent and sneaks back over to you. "Anyway,
# the second column says how the round needs to end: X means you need to lose, Y
# means you need to end the round in a draw, and Z means you need to win. Good
# luck!"
#
# The total score is still calculated in the same way, but now you need to
# figure out what shape to choose so the round ends as indicated. The example
# above now goes like this:
#
# - In the first round, your opponent will choose Rock (A), and you need the
#   round to end in a draw (Y), so you also choose Rock. This gives you a score
#   of 1 + 3 = 4.
# - In the second round, your opponent will choose Paper (B), and you choose
#   Rock so you lose (X) with a score of 1 + 0 = 1.
# - In the third round, you will defeat your opponent's Scissors with Rock for a
#   score of 1 + 6 = 7.
#
# Now that you're correctly decrypting the ultra top secret strategy guide, you
# would get a total score of 12.
#
# Following the Elf's instructions for the second column, what would your total
# score be if everything goes exactly according to your strategy guide?

losing_move = {
    # rock defeats scissor
    "A": "Z",
    # paper defeats rock
    "B": "X",
    # scissor defeats paper]
    "C": "Y",
}

drawing_move = {"A": "X", "B": "Y", "C": "Z"}

winning_move = {
    # rock defeats scissor
    "C": "X",
    # paper defeats rock
    "A": "Y",
    # scissor defeats paper]
    "B": "Z",
}


def part2(inp: str):
    lose = "X"
    draw = "Y"
    win = "Z"

    scores = []

    for line in inp.split("\n"):
        opponent, outcome = line.split(" ")
        if opponent not in ("A", "B", "C") or outcome not in ("X", "Y", "Z"):
            raise ValueError(f"bad parsing: {opponent} {outcome}")

        # figure out what my move must be
        if outcome == lose:
            me = losing_move[opponent]
        elif outcome == draw:
            me = drawing_move[opponent]
        else:
            me = winning_move[opponent]
        score = move_scores[me] + outcome_score(opponent, me)
        scores.append(score)
    return sum(scores)
