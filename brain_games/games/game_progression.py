from random import randint

# Define constants
QUESTION_TEXT = 'What number is missing in the progression?'
PROGRESSION_FIRST_DIGIT_MIN = 1
PROGRESSION_FIRST_DIGIT_MAX = 25
PROGRESSION_STEP_MIN = 5
PROGRESSION_STEP_MAX = 10
PROGRESSION_LENGTH = 10

def get_question_and_answer():
    """
    Function to generate a question and its answer for finding the missing number in a progression.
    The progression starts with a random first number and continues with a constant step.
    
    Returns:
        question (str): The progression string with one number replaced by '..'.
        answer (str): The missing number in the progression as a string.
    """
    progression = []
    first_number = randint(PROGRESSION_FIRST_DIGIT_MIN, PROGRESSION_FIRST_DIGIT_MAX)
    progression.append(first_number)
    progression_step = randint(PROGRESSION_STEP_MIN, PROGRESSION_STEP_MAX)

    for _ in range(PROGRESSION_LENGTH - 1):  # Subtract 1 because the first number is already added
        progression.append(progression[-1] + progression_step)

    missing_index = randint(0, len(progression) - 1)
    answer = progression[missing_index]
    progression[missing_index] = '..'

    formatted_progression = ' '.join(map(str, progression))

    return formatted_progression, str(answer)
