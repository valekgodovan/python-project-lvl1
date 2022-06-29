"""The welcome script."""
import prompt


def welcome_user():
    """Welcome user."""  # noqa: DAR201
    return 'Welcome to the Brain Games!'


def name_question():
    """Ask name question."""  # noqa: DAR201
    name = prompt.string('May I have your name? ')
    print('Hello,', name, '!')
