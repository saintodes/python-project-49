from prompt import string


def play_round(username, question_and_answer):
    question, correct_answer = question_and_answer()

    print(f"Question: {question}")

    user_answer = string("Your answer: ")

    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        return True

    print(
        f"'{user_answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'"
        f"\nLet's try again, {username}!")

    return False


def run_game(task, question_and_answer):
    correct_answers = 0

    print("Welcome to the Brain Games!")
    username = string("May I have your name? ")
    print(f"Hello, {username}!")
    print(f"{task}")

    while correct_answers != 3:
        round_result = play_round(username, question_and_answer)
        if not round_result:
            print(f"Thank you for playing, {username}!")
        correct_answers += 1

    print(f"Congratulations, {username}!")


def welcome_user():
    name = string("May I have your name? ")

    print(f"Hello, {name}!")

    print("Welcome to the Brain Games!")
