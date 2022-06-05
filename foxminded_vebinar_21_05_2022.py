# Game Rock Scissors Paper
from random import choice

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

OPTIONS = [ROCK, SCISSORS, PAPER]
MAPPING = {
    ROCK: SCISSORS,
    SCISSORS: PAPER,
    PAPER: SCISSORS
}


def get_winner(user_val: str, computer_val: str):
    if user_val == computer_val:
        print('DRAW!\n')
    elif MAPPING[user_val] == computer_val:
        print('You win!\n')
    else:
        print('Computer win!\n')


def validate_input(user_val: str):
    return user_val in OPTIONS


while True:
    user_val = input(f'Type one of the values: {", ".join(OPTIONS)} \n')

    if not validate_input(user_val):
        print('Wrong value. Type again.')
        continue

    computer_val = choice(OPTIONS)
    print('Computer value: ', computer_val)

    get_winner(user_val, computer_val)
