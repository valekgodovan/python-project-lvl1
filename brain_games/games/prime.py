"""The brain prime logic."""
import random

from brain_games.game_logic import ask_question, hello_user, wrong_answer


def is_prime(num):
    div = 1
    for i in range(2, num + 1):
        if num % i == 0:
            div = i
            break
    if div == num:
        return 'yes'
    else:
        return 'no'


def prime():
    name = hello_user()
    step_counter = 0
    while step_counter < 3:
        num = random.randint(1, 20)
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        user_answer = ask_question(num)
        correct_answer = is_prime(num)
        if user_answer == correct_answer:
            step_counter += 1
            print('Correct!')
        else:
            wrong_answer(user_answer, correct_answer, name)
            break
    if step_counter == 3:
        print(f'Congratulations, {name}!')
