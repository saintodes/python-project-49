#!/usr/bin/env python3

from prompt import string


def welcome_user():
    name = string("May I have your name? ")

    print(f"Hello, {name}!")

    print("Welcome to the Brain Games!")


def main():
    welcome_user()


if __name__ == '__main__':
    main()
