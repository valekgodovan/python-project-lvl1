#!/usr/bin/env python
"""Main program."""
from brain_games.game_logic import game_logic
from brain_games.games.progression import QUESTION, get_task


def main():
    """Run progression logic."""
    game_logic(QUESTION, get_task)


if __name__ == '__main__':
    main()
