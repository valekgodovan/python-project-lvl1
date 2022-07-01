"""The even game logic."""
import random

from brain_games.game_logic import hello_user, ask_question, wrong_answer


def even():
    name = hello_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    step_counter = 0
    while step_counter < 3:
        num = random.randint(0, 99)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        user_answer = ask_question(num)
        if user_answer == correct_answer:
            step_counter += 1
            print('Correct!')
        else:
            wrong_answer(user_answer, correct_answer, name)
            break
    if step_counter == 3:
        print(f'Congratulations, {name}!')
