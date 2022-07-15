"""The brain prime game logic."""
import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task():
    task = random.randint(0, 50)
    divisor_counter = 0
    for i in range(2, task // 2 + 1):
        if task % i == 0:
            divisor_counter += 1
            break
    if divisor_counter == 0:
        correct_answer = 'yes'
        return task, correct_answer
    else:
        correct_answer = 'no'
        return task, correct_answer
