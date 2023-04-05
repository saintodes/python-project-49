from random import randint

QUESTION_TEXT = 'What number is missing in the progression?'


def get_question_and_answer():
    numeric_progression = []
    progression_first_digit_random_from = 1
    progression_first_digit_random_to = 25
    progression_step_random_from = 5
    progression_step_random_to = 10

    first_number = randint(
        progression_first_digit_random_from,
        progression_first_digit_random_to
    )
    numeric_progression.append(first_number)
    progression_step = randint(
        progression_step_random_from,
        progression_step_random_to
    )

    for _ in range(9):
        numeric_progression.append(numeric_progression[-1] + progression_step)

    random_index = randint(0, len(numeric_progression) - 1)
    answer = numeric_progression[random_index]
    numeric_progression[random_index] = '..'

    formatted_progression = ' '.join(map(str, numeric_progression))

    return formatted_progression, str(answer)
