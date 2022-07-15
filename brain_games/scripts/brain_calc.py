#!/usr/bin/env python
"""Main program."""
from brain_games.game_logic import game_logic
from brain_games.games.calc import get_task, QUESTION


def main():
    """Run calculator logic."""
    game_logic(QUESTION, get_task)


if __name__ == '__main__':
    main()
