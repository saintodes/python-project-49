#!/usr/bin/env python3
# Bran-game calculations.
# Behold a game that called "Calculator"!.
# The essence of the game is as follows: a user is shown a random mathematical
# expression with two variables that needs to be calculated, and the correct
# answer must be written down.If the player answers
# correctly, they move on to the next round. There are a total of 3
#  rounds. If the player answers incorrectly, the game ends.
# logic:
# 0 Creating games played counter that can't be more than 3.
# 1 Welcoming user.
# 2 Telling rules and asking a question.
# 3 Counting right answer.
# 4 Receiving user's answer.
# 5 Comparing user's to correct answer.
# 6.1.1 If true games played counter increases to 1.
# 6.1.2 If games played counter == 3 game ends with congratulations.
# 6.2 If false game ends.
import random

from prompt import integer
from random import randint
from brain_games.game_engine import welcome_user
from random import choice

games_played_counter = 0


def get_correct_answer():
    digit_1 = randint(1, 10)
    digit_2 = randint(1, 10)
    operator = random.choice(('+', '-', '*'))
    if operator == '+':
        correct_answer = digit_1 + digit_2
    if operator == '-':
        correct_answer = digit_1 - digit_2
    if operator == '*':
        correct_answer = digit_1 * digit_2
    return digit_1, digit_2, operator, correct_answer


def print_rules_and_question():
    digit_1, digit_2, operator = get_correct_answer()
    print('What is the result of the expression? ')
    print(f'Question: {digit_1} {operator} {digit_2}')


def get_user_answer():
    global user_answer
    user_answer = integer('Your answer: ')


def compare_results():
    correct_answer = get_correct_answer()
    name = welcome_user()
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
    global games_played_counter
    name = welcome_user()
    while games_played_counter != 3:
        get_correct_answer()
        print_rules_and_question()
        get_user_answer()
        compare_results()


if __name__ == '__main__':
    main()
