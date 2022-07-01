import random

from brain_games.game_logic import hello_user, wrong_answer


def calc():
    name = hello_user()
    print('What is the result of the expression?')
    step_counter = 0
    while step_counter < 3:
        num_1 = random.randint(0, 10)
        num_2 = random.randint(0, 10)
        char = random.choice(['+', '-', '*'])
        if char == '+':
            print(f'Question: {num_1} + {num_2}')
            correct_answer = str(num_1 + num_2)
        elif char == '-':
            print(f'Question: {num_1} - {num_2}')
            correct_answer = str(num_1 - num_2)
        else:
            print(f'Question: {num_1} * {num_2}')
            correct_answer = str(num_1 * num_2)
        print('Your answer:', end=' ')
        user_answer = input()
        if user_answer == correct_answer:
            step_counter += 1
            print('Correct!')
        else:
            wrong_answer(user_answer, correct_answer, name)
            break
    if step_counter == 3:
        print(f'Congratulations, {name}!')
