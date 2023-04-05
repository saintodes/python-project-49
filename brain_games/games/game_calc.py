#Calculation game.
#
from random import randint, choice
from operator import add, sub, mul

QUESTION_TEXT = 'What is the result of the expression? '

def get_question_and_answer():
    difficullty_min = 1
    difficullty_max = 10
    value1 = randint(difficullty_min, difficullty_max)
    value2 = randint(difficullty_min, difficullty_max)
    operations = (
        ('+', add),
        ('-', sub),
        ('*', mul)
    )
    operation_name, operation = choice(operations)
    question = f'{value1} {operation_name} {value2} OLOLOLO'
    answer = operation(value1, value2)
    return question, str(answer)