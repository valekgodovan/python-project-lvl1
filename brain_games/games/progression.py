"""The brain progression game logic."""
import random

from brain_games.game_logic import ask_question, hello_user, wrong_answer


def get_progression():
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
    return (str_progr, correct_answer)


def progression():
    name = hello_user()
    step_counter = 0
    while step_counter < 3:
        new_progression, correct_answer = get_progression()
        user_answer = ask_question(new_progression)
        if user_answer == correct_answer:
            step_counter += 1
            print('Correct!')
        else:
            wrong_answer(user_answer, correct_answer, name)
            break
    if step_counter == 3:
        print(f'Congratulations, {name}!')
