from operator import add, sub, mul
from random import randint, choice

QUESTION_TEXT = 'What is the result of the expression? '

DIFFICULTY_MIN = 1
DIFFICULTY_MAX = 10

OPERATIONS = (
    ('+', add),
    ('-', sub),
    ('*', mul)
)

def generate_question_and_answer(difficulty_min=DIFFICULTY_MIN, difficulty_max=DIFFICULTY_MAX):
    """
    Generate a mathematical question and its answer.
    
    Parameters:
        difficulty_min (int): The minimum value for the random numbers. Default is 1.
        difficulty_max (int): The maximum value for the random numbers. Default is 10.
    
    Returns:
        str: The mathematical expression as a question.
        str: The answer to the mathematical expression as a string.
    """
    num1 = randint(difficulty_min, difficulty_max)
    num2 = randint(difficulty_min, difficulty_max)
    symbol, operation = choice(OPERATIONS)
    question = f'{num1} {symbol} {num2}'
    answer = operation(num1, num2)
    return question, str(answer)
