from random import randint
from brain_games.cli import welcome_user


def is_even_check_game():
    from brain_games.cli import name
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_even_game_attempt_counter = 0
    while is_even_game_attempt_counter != 3:
        random_number_from0to100 = randint(0, 100)
        if random_number_from0to100 % 2 == 0:
            is_even_game_right_answer = 'yes'
        else:
            is_even_game_right_answer = 'no'

        print(f'Question: {random_number_from0to100}')
        is_even_game_answer = input('Your answer:')

        if is_even_game_answer == is_even_game_right_answer:
            print('Correct!')
            is_even_game_attempt_counter += 1
            if is_even_game_attempt_counter == 3:
                print(f'Congratulations, {name}')
        else:
            print(f"'{is_even_game_answer}' is wrong answer"
                  f" ;(. Correct was '{is_even_game_right_answer}'")
            print(f"Let's try again, {name}")
            break


def main():
    welcome_user()
    is_even_check_game()


if __name__ == '__main__':
    main()
