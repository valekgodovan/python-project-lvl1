#!/usr/bin/env python
"""Main program."""
from brain_games.cli import name_question, welcome_user


def main():
    """Run main."""
    print(welcome_user())
    name_question()


if __name__ == '__main__':
    main()
