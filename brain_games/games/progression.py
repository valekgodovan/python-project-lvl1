"""The brain progression game logic."""
import random

from brain_games.game_logic import game_logic


def get_task():
    first_term = random.randint(0, 10)
    difference = random.randint(1, 5)
    missing_term = random.randint(0, 9)
    list_progression = []
    term = first_term
    for i in range(10):
        list_progression.append(term)
        term += difference
    correct_answer = str(list_progression[missing_term])
    list_progression[missing_term] = '..'
    list_progression = [str(i) for i in list_progression]
    str_progr = ' '.join(list_progression)
    task = str_progr
    return task, correct_answer


def progression():
    question = 'What number is missing in the progression?'
    game_logic(question, get_task)
