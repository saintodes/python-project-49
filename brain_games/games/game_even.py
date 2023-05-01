from random import randint

# Define constants
QUESTION_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
DIFFICULTY_MIN = 1
DIFFICULTY_MAX = 100


def get_question_and_answer():
    """
    Function to generate a question and its answer for
    determining if a number is even or odd. The number
    is randomly chosen based on the defined difficulty (min, max).

    Returns:
        question (int): The randomly chosen number.
        answer (str): 'yes' if the number is even, 'no' otherwise.
    """
    number = randint(DIFFICULTY_MIN, DIFFICULTY_MAX)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer
