from operator import add, sub, mul
from random import randint, choice

# Define constants
QUESTION_TEXT = 'What is the result of the expression? '
DIFFICULTY_MIN = 1
DIFFICULTY_MAX = 10
OPERATIONS = (
    ('+', add),
    ('-', sub),
    ('*', mul)
)

def get_question_and_answer():
    """
    Function to generate a question and its answer for a calculation game.
    The question is a simple arithmetic operation (addition, subtraction, multiplication)
    with operands randomly chosen based on the defined difficulty (min, max).
    
    Returns:
        question (str): The arithmetic operation as a string.
        answer (str): The result of the arithmetic operation as a string.
    """
    operand1 = randint(DIFFICULTY_MIN, DIFFICULTY_MAX)
    operand2 = randint(DIFFICULTY_MIN, DIFFICULTY_MAX)
    operation_symbol, operation_func = choice(OPERATIONS)
    question = f'{operand1} {operation_symbol} {operand2}'
    answer = operation_func(operand1, operand2)
    return question, str(answer)
