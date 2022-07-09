"""The great common divisor game logic."""
import random

from brain_games.game_logic import game_logic


def get_task():
    num_1 = random.randint(0, 50)
    num_2 = random.randint(0, 50)
    task = f'{num_1} {num_2}'
    divisor = 1
    if num_1 >= num_2:
        big_num = num_1
    else:
        big_num = num_2
    for i in range(1, big_num + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            divisor = str(i)
    return task, divisor


def gcd():
    question = 'Find the greatest common divisor of given numbers.'
    game_logic(question, get_task)
