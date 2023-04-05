#
#
#
from random import randint

QUESTION_TEXT = 'What number is missing in the progression?'

def get_question_and_answer():
    numberic_progression = []
    progression_first_digit_random_from = 1
    progression_first_digit_random_to = 25
    progression_step_random_from = 5
    progression_step_random_to = 10
    
    first_number = randint(progression_first_digit_random_from, progression_first_digit_random_to)
    
    numberic_progression.append(first_number)
    progression_step = randint(progression_step_random_from, progression_step_random_to)
    while len(numberic_progression) != 10:
        numberic_progression.append(numberic_progression[-1]
                                    + progression_step)
    random_index = randint(0, len(numberic_progression) - 1)
    answer = numberic_progression[random_index]
    numberic_progression[random_index] = '..'
    return numberic_progression, str(answer)