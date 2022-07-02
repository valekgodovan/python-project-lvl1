"""The great common divisor game logic."""
import random


from brain_games.game_logic import hello_user, wrong_answer

def find_divisor(num1, num2):
    if num1 <= num2:
        small_num = num1
    else:
        small_num = num2
    for i in range(1, small_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisor = i
    return str(divisor)


def gcd():
    name = hello_user()
    print('Find the greatest common divisor of given numbers.')
    step_counter = 0
    while step_counter < 3:
        num_1 = random.randint(0, 100)
        num_2 = random.randint(0, 100)
        correct_answer = find_divisor(num_1, num_2)
        print(f'Question: {num_1} {num_2}')
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
