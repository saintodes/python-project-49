#!/usr/bin/env python3
# Game "Is_even?".
# The player is shown a random number and they need to answer yes if
# the number is even or no if it's odd. If the player answers
# correctly, they move on to the next round. There are a total of 3
# rounds. If the player answers incorrectly, the game ends.
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
from random import randint
from brain_games.common_logic import welcome_user

games_played_counter = 0


def get_correct_answer():
    global random_number, is_even
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        is_even = 'yes'
    else:
        is_even = 'no'


def print_rules_ask_question():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {random_number}')


def get_user_answer():
    global user_answer
    user_answer = input()


def compare_results():
    global games_played_counter
    if user_answer == is_even:
        print('Correct!')
        games_played_counter += 1
        if games_played_counter == 3:
            print(f'Congratulations, {name}!')
    else:
        print(f'{user_answer} is wrong answer')
        print(f"Let's try again, {name}!")
        games_played_counter = 3


def main():
    global name, games_played_counter
    name = welcome_user()
    while games_played_counter != 3:
        get_correct_answer()
        print_rules_ask_question()
        get_user_answer()
        compare_results()


if __name__ == '__main__':
    main()
