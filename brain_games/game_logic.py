"""The game logic."""
import prompt


def game_logic(question, func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)
    step_counter = 0
    while step_counter < 3:
        task, correct_answer = func()
        print(f'Question: {task}')
        print('Your answer:', end=' ')
        user_answer = input()
        if user_answer == correct_answer:
            step_counter += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if step_counter == 3:
        print(f'Congratulations, {name}!')
