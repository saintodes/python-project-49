#!/usr/bin/env python3
# Program logic is:
# 0 Creating games played counter that in any game can't be more than 3.
# 1 Welcoming user.
# 2 Telling rules and asking a question.
# 3 Counting right answer.
# 4 Receiving user's answer.
# 5 Comparing user's to correct answer.
# 6.1.1 If true games played counter increases to 1.
# 6.1.2 If games played counter == 3 game ends with congratulations.
# 6.2 If false game ends.
from brain_games.common_logic import welcome_user


def main():
    welcome_user()


if __name__ == '__main__':
    main()
