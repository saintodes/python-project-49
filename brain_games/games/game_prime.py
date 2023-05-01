from random import randint

# Define constants
QUESTION_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
DIFFICULTY_MIN = 1
DIFFICULTY_MAX = 10


def is_prime(n):
    """
    Function to check if a number is prime.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_question_and_answer():
    """
    Function to generate a question and its answer
    for determining if a number is prime. The number is
    randomly chosen based on the defined difficulty (min, max).

    Returns:
        question (str): The randomly chosen number as a string.
        answer (str): 'yes' if the number is prime, 'no' otherwise.
    """
    number = randint(DIFFICULTY_MIN, DIFFICULTY_MAX)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
