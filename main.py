# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

import random

# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.

options = ["stone", "paper", "scissors"]

# Assign a variable to the maximum number of games: 1, 3, 5, etc ...

max_games = 5

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games

min_player_win = 3


# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.

def random_options():
    return random.choice(options)


# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.

def ask_choices():
    txt = input("Type 1 of these 3 options: stone, paper, scissors. ")
    while (txt != "stone") and (txt != "paper") and (txt != "scissors"):
        print("Check your spelling!")
        txt = input("Type 1 of these 3 options: stone, paper, scissors. ")
    return txt


# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins

def combat(p, c):
    if p == c:
        return 0
    elif p == "stone":
        if c == "paper":
            return 1
        else:
            return 2
    elif p == "paper":
        if c == "scissors":
            return 1
        else:
            return 2
    elif p == "scissors":
        if c == "stone":
            return 1
        else:
            return 2


# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated

def show(p, c, pa, ca):
   print(p)
   print(c)
   print(pa)
   print(ca)


# Create two variables that accumulate the wins of each participant

player_wins = 0
computer_wins = 0

# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.

i = 0
while i < max_games:
    player = ask_choices()
    computer = random_options()
    result = combat(player, computer)

    if result == 1:
        computer_wins += 1
    elif result == 2:
        player_wins += 1

    show(player, computer, player_wins, computer_wins)

    if player_wins == min_player_win or computer_wins == min_player_win:
        break

    i += 1

# Print by console the winner of the game based on who has more accumulated wins

if computer_wins > player_wins:
    print("You lose!")
else:
    print("You win!")
