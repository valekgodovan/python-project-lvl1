"""The welcome script."""
import prompt


def welcome_user():
    """Welcome user."""  # noqa: DAR201
    return ('Welcome to Brain Games!')


def name_question():
    """Ask a name."""  # noqa: DAR201
    name = prompt.string('May I have your name? ')
    return ('Hello,', name, '!')
