#!/usr/bin/env python
"""Main program."""
from brain_games.games.gcd import get_task, QUESTION
from brain_games.game_logic import game_logic


def main():
    """Run great common divisor logic."""
    game_logic(QUESTION, get_task)


if __name__ == '__main__':
    main()
