from prompt import string

TOTAL_ROUNDS = 3


def run_game(task, question_and_answer, total_rounds=TOTAL_ROUNDS):
    print("Welcome to the Brain Games!")
    username = string("May I have your name? ")
    print(f"Hello, {username}!\n{task}")

    for _ in range(total_rounds):
        question, correct_answer = question_and_answer()
        print(f"Question: {question}")
        user_answer = string("Your answer: ")

        if user_answer.lower() != correct_answer.lower():
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {username}!")
            print("Better luck next time!")
            return

        print("Correct!")



    print(f"Congratulations, {username}!")
