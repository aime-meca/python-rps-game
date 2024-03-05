import random

while True:
    # Section 1: Ask the user for their input

    user_input = input('Rock, Paper, or Scissors: ')
    user_input = user_input.lower()
    if user_input != 'r' and user_input != 'p' and user_input != 's':
        print('Invalid input')
        exit()

    # Section 2: Generate computer response
    MOVES = ['r', 'p', 's']
    computer_move = random.choice(MOVES)

    # Section 3: Compare user vs. computer

    result = None

    # Check for tie
    if user_input == computer_move:
        result = 'tie'
    # Check for user win
    elif user_input == 'r' and computer_move == 's':
        result = 'win'
    elif user_input == 'p' and computer_move == 'r':
        result = 'win'
    elif user_input == 's' and computer_move == 'p':
        result = 'win'
    # Else, user has lost
    else:
        result = 'lose'

    # Section 4: Print result
    print(result)
