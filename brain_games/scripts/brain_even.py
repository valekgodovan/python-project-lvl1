#!/usr/bin/env python
"""Main program."""
from brain_games.game_logic import game_logic
from brain_games.games.even import get_task, QUESTUON


def main():
    """Run even logic."""
    game_logic(QUESTUON, get_task)


if __name__ == '__main__':
    main()
