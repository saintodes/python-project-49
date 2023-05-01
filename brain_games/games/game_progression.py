from random import randint

# Define constants
QUESTION_TEXT = 'What number is missing in the progression?'
FIRST_DIGIT_MIN = 1
FIRST_DIGIT_MAX = 25
STEP_MIN = 5
STEP_MAX = 10
PROGRESSION_LENGTH = 10


def generate_progression(first_number, step, length):
    """
    Function to generate a numeric progression.

    Parameters:
        first_number (int): The first number in the progression.
        step (int): The common difference between all numbers in the progression
        length (int): The total length of the progression.

    Returns:
        list of int: The generated progression.
    """
    return [first_number + i * step for i in range(length)]


def get_question_and_answer():
    """
    Function to generate a question and its answer for finding
    the missing number in a progression. The progression starts
    with a random first number and continues with a constant step.

    Returns:>
        question (str): The progression string with one number replaced by '..'.
        answer (str): The missing number in the progression as a string.
    """
    first_number = randint(FIRST_DIGIT_MIN, FIRST_DIGIT_MAX)
    step = randint(STEP_MIN, STEP_MAX)

    progression = generate_progression(first_number, step, PROGRESSION_LENGTH)

    missing_index = randint(0, len(progression) - 1)
    answer = progression[missing_index]
    progression[missing_index] = '..'

    formatted_progression = ' '.join(map(str, progression))

    return formatted_progression, str(answer)
