import random

VALID_CHOICES = ['rock', 'paper', 'scissors']


def tie_game():
    print("It's a tie! :/")


def player_wins():
    print("You win! :)")


def computer_wins():
    print("The computer wins! :(")


def ask_player_for_choice():
    choice = input('What do you choose (rock, paper, scissors): ').lower()
    return choice


def ask_computer_for_choice():
    choice = random.choice(VALID_CHOICES)
    return choice


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        tie_game()

    elif player_choice == 'rock':
        if computer_choice == 'scissors':
            player_wins()
        elif computer_choice == 'paper':
            computer_wins()

    elif player_choice == 'paper':
        if computer_choice == 'rock':
            player_wins()
        elif computer_choice == 'scissors':
            computer_wins()

    elif player_choice == 'scissors':
        if computer_choice == 'paper':
            player_wins()
        elif computer_choice == 'rock':
            computer_wins()


print("Let's play a game of Rock, Paper Scissors!")
while True:
    player_choice = ask_player_for_choice()
    while player_choice not in VALID_CHOICES:
        player_choice = ask_player_for_choice()

    computer_choice = ask_computer_for_choice()
    determine_winner(player_choice, computer_choice)
    print()
