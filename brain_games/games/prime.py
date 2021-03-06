"""The brain prime game logic."""
import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def get_task():
    task = random.randint(0, 50)
    if is_prime(task):
        correct_answer = 'yes'
        return task, correct_answer
    else:
        correct_answer = 'no'
        return task, correct_answer
