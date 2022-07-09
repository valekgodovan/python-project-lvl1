"""The game logic."""
import prompt


def game_logic(question, game_func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)
    STEP_COUNT = 3
    for _ in range(STEP_COUNT):
        task, correct_answer = game_func()
        print(f'Question: {task}')
        print('Your answer:', end=' ')
        user_answer = input()
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
