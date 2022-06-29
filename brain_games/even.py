"""The even game logic."""
import random

import prompt


def welcome_user():
    """Welcome user."""  # noqa: DAR201
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    step_counter = 0
    while step_counter < 3:
        num = random.randint(0, 999)
        if num % 2 == 0:
            check = 'yes'
        else:
            check = 'no'
        print(f'Question: {num}')
        print('Your answer:', end=' ')
        answer = input()
        if answer == check:
            step_counter += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{check}'.")
            print(f"Let's try again, {name}")
            break
    if step_counter == 3:
        print(f'Congratulations, {name}!')
