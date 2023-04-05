#!/usr/bin/env python3

from math import gcd
from random import randint

QUESTION_TEXT = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    difficullty_min = 1
    difficullty_max = 100
    value1 = randint(difficullty_min, difficullty_max)
    value2 = randint(difficullty_min, difficullty_max)
    question = f'Question: {value1} {value2}'
    answer = gcd(value1, value2)
    return question, str(answer)
