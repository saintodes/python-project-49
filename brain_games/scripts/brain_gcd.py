#!/usr/bin/env python3
from prompt import integer
from math import gcd
from random import randint
from brain_games.common_logic import welcome_user

games_played_counter = 0


def get_correct_answer():
    global correct_answer, digit_1, digit_2
    digit_1 = randint(1, 100)
    digit_2 = randint(1, 100)
    correct_answer = gcd(digit_1, digit_2)


def print_rules_and_question():
    print("Find the greatest common divisor of given numbers.")
    print(f'Question: {digit_1} {digit_2}')


def get_user_answer():
    global user_answer
    user_answer = integer()


def compare_results():
    global games_played_counter
    if correct_answer == user_answer:
        print('Correct!')
        games_played_counter += 1
        if games_played_counter == 3:
            print(f'Congratulations, {name}')
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
