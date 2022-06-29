"""The even game logic."""
import prompt
import random


def welcome_user():
    """Welcome user."""  # noqa: DAR201
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    step_counter = 0
    for i in range(3):
        num = random.randint(0, 99)
        if num % 2 == 0:
            check = 'yes'
        else:
            check = 'no'
        print(f'Question: {num}')
        print('Your answer:', end=' ')
        answer = input()
        if answer == check:
            step_counter += 1
            print(f'Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {check}.')
            print(f'Let\'s try again, {name}')
            break
    if step_counter == 3:
        print(f'Congratulations, {name}!')
