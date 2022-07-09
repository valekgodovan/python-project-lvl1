"""The calculator game logic."""
import random

from brain_games.game_logic import game_logic


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


def calc():
    question = 'What is the result of the expression?'
    game_logic(question, get_task)    
