"""The game logic."""
import prompt


def hello_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(task):
    print(f'Question: {task}')
    print('Your answer:', end=' ')
    user_answer = input()
    return user_answer


def wrong_answer(user_answer, correct_answer, name):
    print(f"'{user_answer}' is wrong answer ;(.", end=' ')
    print(f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")


def game_logic(question, task, correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)
    print(f'Question: {task}')
    print('Your answer:', end=' ')
    user_answer = input()
    step_counter = 0
    while step_counter < 3:
        if user_answer == correct_answer:
            step_counter += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
    if step_counter == 3:
        print(f'Congratulations, {name}!')
