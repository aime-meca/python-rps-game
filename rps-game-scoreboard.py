import random

# List of valid choices for the game
VALID_CHOICES = ['rock', 'paper', 'scissors']

# Scoreboard variables
NUM_WINS = 0
NUM_LOSSES = 0
NUM_TIES = 0


# What to do when the game results in a tie
def tie_game():
    global NUM_TIES
    print("It's a tie! :/")
    NUM_TIES += 1


# What to do when the game results in the player winning
def player_wins():
    global NUM_WINS
    print("You win! :)")
    NUM_WINS += 1


# What to do when the game results in the computer winning
def computer_wins():
    global NUM_LOSSES
    print("The computer wins! :(")
    NUM_LOSSES += 1


# Get the choice from the player
def ask_player_for_choice():
    choice = input('What do you choose (rock, paper, scissors): ').lower()
    return choice


# Get the choice from the computer
def ask_computer_for_choice():
    choice = random.choice(VALID_CHOICES)
    return choice


# Determine who won based on both the player's and computer's choices
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


# Main game loop that runs forever
print("Let's play a game of Rock, Paper, Scissors!")
while True:
    try:
        player_choice = ask_player_for_choice()
        while player_choice not in VALID_CHOICES:
            player_choice = ask_player_for_choice()

        computer_choice = ask_computer_for_choice()
        determine_winner(player_choice, computer_choice)
        print()
    except KeyboardInterrupt:
        print()
        print()
        print('Summary of results')
        print(f'Number of wins: {NUM_WINS}')
        print(f'Number of losses: {NUM_LOSSES}')
        print(f'Number of ties: {NUM_TIES}')
        exit()
