#!/usr/bin/env python
"""Main program."""
from brain_games.game_logic import run_game
from brain_games.games.prime import get_task, QUESTION


def main():
    """Run great common divisor logic."""
    run_game(QUESTION, get_task)


if __name__ == '__main__':
    main()
