# Importing required modules
from prompt import string


# Function to run the game
def run_game(task, question_and_answer):
    # Printing welcome message
    print('Welcome to the Brain Games!')

    # Asking the user for their name
    username = string('May I have your name? ')

    # Printing personalized welcome message
    print(f'Hello, {username}!')

    # Printing task description
    print(f'{task}')

    # Function to play a round of game
    def play_round():
        # Fetching question and correct answer
        question, correct_answer = question_and_answer()

        # Displaying question
        print(f'Question: {question}')

        # Accepting user's answer
        user_answer = string('Your answer: ')

        # Asserting if user's answer is equal to correct answer
        assert user_answer.lower() == correct_answer.lower(), \
            f"'{user_answer}' is wrong answer ;(. " \
            f"Correct answer was '{correct_answer}'" \
            f"\nLet's try again, {username}!"

        # Printing correct answer message
        print('Correct!')

        # Returning True for correct answer
        return True

    # Running game for 3 rounds
    try:
        sum(play_round() for _ in range(3))

        # Printing congratulations message on successfully playing 3 rounds
        print(f'Congratulations, {username}!')

    # Catching AssertionError if any, which is raised when user's answer
    # doesn't match correct answer
    except AssertionError as error:
        # Printing error message
        print(error)

# Function to welcome the user


def welcome_user():
    # Asking the user for their name
    name = string('May I have your name? ')

    # Printing personalized welcome message
    print(f'Hello, {name}!')

    # Printing welcome message for the game
    print('Welcome to the Brain Games!')
