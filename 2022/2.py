import sys
from pathlib import Path
from typing import Tuple

"""
https://adventofcode.com/2022/day/2
"""


def main() -> Tuple[int, int]:  # why can't I use tuple(int, int) ?
    """Return score"""
    debug = True
    score_total_part_1 = 0
    score_total_part_2 = 0
    file_name = Path(__file__).parent / "2.txt"  # each input differs by user
    with open(file_name) as fh:
        for line in fh:
            input_1, input_2 = line.strip().split(" ")
            if debug:
                print(f"input 1: {input_1}, input 2: {input_2}")
            score_total_part_1 += score_round_part_1(play_opponent=input_1, play_you=input_2)
            score_total_part_2 += score_round_part_2(play_opponent=input_1, desired_outcome=input_2)

    return score_total_part_1, score_total_part_2


def score_round_part_1(play_opponent: str, play_you: str) -> int:
    """
    Input file has opponent play and your play per line:
    A = opponent rock
    B = opponent paper
    C = opponent scissors
    X = you rock
    Y = you paper
    Z = you scissors

    Points:
    rock = 1 point
    paper = 2 points
    scissor = 3 points
    loss = 0 points
    draw = 3 points
    win = 6 points

    :param play_opponent: str
    :param play_you: str
    :return: score
    """
    SCORE_ROCK: int = 1
    SCORE_PAPER: int = 2
    SCORE_SCISSORS: int = 3
    SCORE_LOSS: int = 0
    SCORE_DRAW: int = 3
    SCORE_WIN: int = 6
    ROCK: list = ['A', 'X']
    PAPER: list = ['B', 'Y']
    SCISSORS: list = ['C', 'Z']

    score = 0

    if play_you in ROCK:
        score += SCORE_ROCK
        if play_opponent in ROCK:
            score += SCORE_DRAW
        elif play_opponent in PAPER:
            score += SCORE_LOSS
        elif play_opponent in SCISSORS:
            score += SCORE_WIN
        else:
            print(f"Unknown opponent play: {play_opponent}")
            sys.exit(1)
    elif play_you in PAPER:
        score += SCORE_PAPER
        if play_opponent in ROCK:
            score += SCORE_WIN
        elif play_opponent in PAPER:
            score += SCORE_DRAW
        elif play_opponent in SCISSORS:
            score += SCORE_LOSS
        else:
            print(f"Unknown opponent play: {play_opponent}")
            sys.exit(1)
    elif play_you in SCISSORS:
        score += SCORE_SCISSORS
        if play_opponent in ROCK:
            score += SCORE_LOSS
        elif play_opponent in PAPER:
            score += SCORE_WIN
        elif play_opponent in SCISSORS:
            score += SCORE_DRAW
        else:
            print(f"Unknown opponent play: {play_opponent}")
            sys.exit(1)
    else:
        print(f"Unknown you play: {play_you}")
        sys.exit(2)
    return score


def score_round_part_2(play_opponent: str, desired_outcome: str) -> int:
    """
    Input file has opponent play and desired outcome per line:
    A = opponent rock
    B = opponent paper
    C = opponent scissors
    X = desired outcome loss
    Y = desired outcome draw
    Z = desired outcome win

    Points:
    rock = 1 point
    paper = 2 points
    scissor = 3 points
    loss = 0 points
    draw = 3 points
    win = 6 points

    :param play_opponent: str
    :param desired_outcome: str
    :return: score
    """
    SCORE_ROCK: int = 1
    SCORE_PAPER: int = 2
    SCORE_SCISSORS: int = 3
    SCORE_LOSS: int = 0
    SCORE_DRAW: int = 3
    SCORE_WIN: int = 6
    ROCK: str = 'A'
    PAPER: str = 'B'
    SCISSORS: str = 'C'
    LOSS: str = 'X'
    DRAW: str = 'Y'
    WIN: str = 'Z'

    score = 0

    if desired_outcome == LOSS:
        score += SCORE_LOSS
        if play_opponent in ROCK:
            score += SCORE_SCISSORS
        elif play_opponent in PAPER:
            score += SCORE_ROCK
        elif play_opponent in SCISSORS:
            score += SCORE_PAPER
        else:
            print(f"Unknown opponent play: {play_opponent}")
            sys.exit(3)
    elif desired_outcome == DRAW:
        score += SCORE_DRAW
        if play_opponent in ROCK:
            score += SCORE_ROCK
        elif play_opponent in PAPER:
            score += SCORE_PAPER
        elif play_opponent in SCISSORS:
            score += SCORE_SCISSORS
        else:
            print(f"Unknown opponent play: {play_opponent}")
            sys.exit(3)
    elif desired_outcome == WIN:
        score += SCORE_WIN
        if play_opponent in ROCK:
            score += SCORE_PAPER
        elif play_opponent in PAPER:
            score += SCORE_SCISSORS
        elif play_opponent in SCISSORS:
            score += SCORE_ROCK
        else:
            print(f"Unknown opponent play: {play_opponent}")
            sys.exit(3)
    else:
        print(f"Unknown desired outcome: {desired_outcome}")
        sys.exit(4)
    return score


if __name__ == '__main__':
    print(main())
else:
    print("This is meant to be run directly and never imported.")
    sys.exit(5)
