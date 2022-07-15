"""The great common divisor game logic."""
import random


QUESTION = 'Find the greatest common divisor of given numbers.'


def get_divisor(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return get_divisor(num_2, num_1 % num_2)


def get_task():
    num_1 = random.randint(0, 50)
    num_2 = random.randint(0, 50)
    task = f'{num_1} {num_2}'
    divisor = str(get_divisor(num_1, num_2))
    return task, divisor
