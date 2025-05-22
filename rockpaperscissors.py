# software development method: Rock paper scissors is a game where the player is given a choice to choose rock, paper, or scissors
# then, the computer player, or "enemy" randomly chooses their move, and then we determine who won and display a "You won!"" or a "You lost!"  message to the player

import random
print("Welcome to Rock Paper Scissors")
print("Please choose 1, 2, or 3 to select Rock, Paper, or Scissors: ")
player_choice = input()
if(not player_choice.isdigit()):
    print("Didn't you want to play the game? Try Again.")
    exit()

if (int(player_choice) > 3 or int(player_choice) < 1):
    print("Let's try to stick with 1, 2, or 3.")
    exit()
# we could generate the computer player's
# move choice here too
player_choice = int(player_choice)
ai_choice = random.randint(1, 3)
moves_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}
# we look up the associated strings in the moves dictionary
# by using the dictionary[a key value]
ai_choice_string = moves_dict[ai_choice]
player_choice_string = moves_dict[player_choice]
print(f"You chose: {player_choice_string}")
print(f"The Enemy chose: {ai_choice_string}")
if ((player_choice == 1 and ai_choice == 3) or (player_choice == 2 and ai_choice == 1) or (player_choice == 3 and ai_choice == 2)): 
    print("Smart choice, you win!")
elif ((player_choice == 1 and ai_choice == 1) or (player_choice == 2 and ai_choice == 2) or (player_choice == 3 and ai_choice == 3)): 
    print("It's a tie! Better try again.")
else:
    print("You have failed! Better luck next time partner.")