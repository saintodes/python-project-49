from prompt import string


def run_game(task, question_and_answer):
    print('Welcome to the Brain Games!')
    username = string('May I have your name? ')
    print(f'Hello, {username}!')
    print(f'{task}')  # объявляем задание
    games_played_counter = 0
    while games_played_counter != 3:
        question, correct_answer = question_and_answer()
        print(f'{question}')
        user_answer = string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            games_played_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {username}")
    print(f'Congratulations, {username}!')


def welcome_user():
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Welcome to the Brain Games!')
