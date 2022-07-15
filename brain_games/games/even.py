"""The even game logic."""
import random


QUESTUON = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task():
    task = random.randint(0, 99)
    if task % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (task, correct_answer)
