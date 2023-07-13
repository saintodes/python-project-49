from prompt import string

TOTAL_ROUNDS = 3


def get_input(prompt_message):
    return string(prompt_message)


def welcome_message(task):
    print("Welcome to the Brain Games!")
    username = get_input("May I have your name? ")
    print(f"Hello, {username}!\n{task}")
    return username


def play_round(question_and_answer):
    question, correct_answer = question_and_answer()
    print(f"Question: {question}")
    user_answer = get_input("Your answer: ")

    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        return True

    print(
        f"'{user_answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'")
    return False


def play_game(username, question_and_answer, total_rounds=TOTAL_ROUNDS):
    rounds_won = 0

    for _ in range(total_rounds):
        if not play_round(question_and_answer):
            print(f"Let's try again, {username}!")
            return False

        rounds_won += 1

    return True


def final_message(game_won, username):
    print(f"Congratulations, {username}!" if game_won
          else "Better luck next time!")


def run_game(task, question_and_answer, total_rounds=3):
    username = welcome_message(task)
    game_result = play_game(username, question_and_answer, total_rounds)
    final_message(game_result, username)
