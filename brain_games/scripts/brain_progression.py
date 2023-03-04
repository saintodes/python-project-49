#!/usr/bin/env python3
from prompt import integer
from random import randint
from brain_games.common_logic import welcome_user

games_played_counter = 0


def get_correct_answer():
    global numberic_progression, correct_answer
    first_number = randint(1, 25)
    numberic_progression = []
    numberic_progression.append(first_number)
    progression_step = randint(5, 10)
    while len(numberic_progression) != 10:
        numberic_progression.append(numberic_progression[-1]
                                    + progression_step)
    random_index = randint(0, len(numberic_progression) - 1)
    correct_answer = numberic_progression[random_index]
    numberic_progression[random_index] = '..'


def print_rules_and_question():
    print('What number is missing in the progression?')
    print(numberic_progression)
    pass


def get_user_answer():
    global user_answer
    user_answer = integer()


def compare_results():
    global games_played_counter
    if correct_answer == user_answer:
        print('Correct!')
        games_played_counter += 1
        if games_played_counter == 3:
            print(f'Congratulations, {name}!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}")
        games_played_counter = 3


def main():
    global games_played_counter, name
    name = welcome_user()
    while games_played_counter != 3:
        get_correct_answer()
        print_rules_and_question()
        get_user_answer()
        compare_results()


if __name__ == '__main__':
    main()
