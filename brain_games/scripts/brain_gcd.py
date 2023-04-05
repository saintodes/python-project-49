#!/usr/bin/env python3

from brain_games.common_games_engine import run_game
from brain_games.games.game_gcd import QUESTION_TEXT, get_question_and_answer

def main():
    run_game(QUESTION_TEXT, get_question_and_answer)

if __name__ == ' __main__':
    main()