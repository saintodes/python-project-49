# Importing required modules
from prompt import string

# Function to run a single round of the game
def play_round(username, question_and_answer):
    # Fetching question and correct answer
    question, correct_answer = question_and_answer()

    # Displaying question
    print(f'Question: {question}')

    # Accepting user's answer
    user_answer = string('Your answer: ')

    # Check if user's answer is equal to correct answer
    if user_answer.lower() == correct_answer.lower():
        # Printing correct answer message
        print('Correct!')
        # Returning True for correct answer
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. " \
            f"Correct answer was '{correct_answer}'" \
            f"\nLet's try again, {username}!")
        return False

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

    # Running game for 3 rounds
    correct_answers = 0
    for _ in range(3):
        correct = play_round(username, question_and_answer)
        if correct:
            correct_answers += 1
        else:
            break

    if correct_answers == 3:
        # Printing congratulations message on successfully playing 3 rounds
        print(f'Congratulations, {username}!')
    else:
        print(f'Thank you for playing, {username}!')

# Function to welcome the user
def welcome_user():
    # Asking the user for their name
    name = string('May I have your name? ')

    # Printing personalized welcome message
    print(f'Hello, {name}!')

    # Printing welcome message for the game
    print('Welcome to the Brain Games!')
