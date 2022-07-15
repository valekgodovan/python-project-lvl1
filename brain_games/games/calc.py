"""The calculator game logic."""
import random


QUESTION = 'What is the result of the expression?'


def get_task():
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    char = random.choice(['+', '-', '*'])
    if char == '+':
        task = f'{num_1} + {num_2}'
        correct_answer = str(num_1 + num_2)
    elif char == '-':
        task = f'{num_1} - {num_2}'
        correct_answer = str(num_1 - num_2)
    else:
        task = f'{num_1} * {num_2}'
        correct_answer = str(num_1 * num_2)
    return (task, correct_answer)
