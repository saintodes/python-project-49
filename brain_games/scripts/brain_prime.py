#!/usr/bin/env python3
from random import randint
from brain_games.game_engine import welcome_user

games_played_counter = 0


def get_correct_answer():
    global correct_answer, digit
    digit = randint(1, 10)
    count = 0
    for i in range(1, digit + 1):
        if digit % i == 0:
            count += 1
    if count == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'


def print_rules_and_question():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {digit}')


def get_user_answer():
    global user_answer
    user_answer = input()


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
