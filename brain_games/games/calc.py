"""The calculator game logic."""
import random
import operator


QUESTION = 'What is the result of the expression?'


def get_task():
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operation = random.choice(list(operations.keys()))
    correct_answer = str(operations[operation](num_1, num_2))
    task = f'{num_1} {operation} {num_2}'
    return (task, correct_answer)
