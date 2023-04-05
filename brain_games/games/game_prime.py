#!/usr/bin/env python3

from random import randint

QUESTION_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    divider_count = 0
    difficullty_min = 1
    difficullty_max = 10
    value = randint(difficullty_min, difficullty_max)
    question = f'{value}'
    for divider in range(1, value + 1):
        if value % divider == 0:
            divider_count += 1
    if divider_count == 2:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
