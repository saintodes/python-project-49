#
#
#
from random import randint

QUESTION_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    difficullty_min = 1
    difficullty_max = 100
    question = randint(difficullty_min, difficullty_max)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
