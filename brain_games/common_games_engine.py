from prompt import string

global name


# 0 Creating games played counter.
# 1 Welcoming user
# 2 Telling rules and asking question.
# 3 Counting right answer.
# 4 Receiving users answer.
# 5 Comparing users to right answer.
# 6.1 If true games played counter increases to 1
# 6.2 if false game ends
# 7 Repeat steps 2 - 6.2
# 8  If games played counter == 3 : printing endings, game ends.


def run_game():
    print('Welcome to the Brain Games!')
    username = string('May I have your name? ')
    print(f'Hello, {username}!')
    print(f'')#объявляем задание
    games_played_counter = 0
    while games_played_counter != 3:
        question, correct_answer = get_correct_answer()
        print(f'{question}')
        user_answer = prompt.string('Your answer:')
        if user_answer == correct_answer:
            print('Correct!')
            games_played_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                 f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}")
    print(f'Congratulations, {name}!')