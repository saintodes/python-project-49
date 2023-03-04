#!/usr/bin/env python3
from prompt import integer
from random import randint
from brain_games.common_logic import welcome_user

games_played_counter = 0


def get_correct_answer():
    global operator_sign, digit_1, digit_2, correct_answer
    digit_1 = randint(1, 10)
    digit_2 = randint(1, 10)
    operator = randint(1, 3)
    if operator == 1:
        correct_answer = digit_1 + digit_2
        operator_sign = '+'
    if operator == 2:
        correct_answer = digit_1 - digit_2
        operator_sign = '-'
    if operator == 3:
        correct_answer = digit_1 * digit_2
        operator_sign = '*'
    # print(f'__________d1 = {digit_1}, d2 = {digit_2}')
    # print(f'__________correct answer is {correct_answer} '
    #       f'and sign (+ or - or /) is {operator_sign}')


def print_rules_and_question():
    print('What is the result of the expression? ')
    print(f'{digit_1} {operator_sign} {digit_2}')


def get_user_answer():
    global user_answer
    user_answer = integer('Your answer: ')


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
