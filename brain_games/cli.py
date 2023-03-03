import prompt


def welcome_user():
    print('Whelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


welcome_user()
