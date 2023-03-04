import prompt
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


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

