from math import gcd
from random import randint

# Define constants
QUESTION_TEXT = 'Find the greatest common divisor of given numbers.'
DIFFICULTY_MIN = 1
DIFFICULTY_MAX = 100

def get_question_and_answer():
    """
    Function to generate a question and its answer for finding the greatest common divisor.
    The question includes two numbers randomly chosen based on the defined difficulty (min, max).
    
    Returns:
        question (str): The question string including two numbers.
        answer (str): The greatest common divisor of the two numbers as a string.
    """
    number1 = randint(DIFFICULTY_MIN, DIFFICULTY_MAX)
    number2 = randint(DIFFICULTY_MIN, DIFFICULTY_MAX)
    question = f'Question: {number1} {number2}'
    answer = gcd(number1, number2)
    return question, str(answer)
