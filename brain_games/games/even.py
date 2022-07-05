"""The even game logic."""
import random

from brain_games.game_logic import game_logic


def give_task():
    task = random.randint(0, 99)
    if task % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (task, correct_answer)


def even():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_logic(question, give_task)
