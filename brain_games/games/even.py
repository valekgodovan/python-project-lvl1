"""The even game logic."""
import random


QUESTUON = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task():
    task = random.randint(0, 99)
    correct_answer = 'no' if task % 2 else 'yes'
    return task, correct_answer
