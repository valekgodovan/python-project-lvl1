"""The brain prime game logic."""
import random

from brain_games.game_logic import game_logic


def get_task():
    task = random.randint(0, 50)
    divisor = 1
    for i in range(2, task + 1):
        if task % i == 0:
            divisor = i
            break
    if divisor == task:
        correct_answer = 'yes'
        return task, correct_answer
    else:
        correct_answer = 'no'
        return task, correct_answer


def prime():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_logic(question, get_task)
