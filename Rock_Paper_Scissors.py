import random

edi_choices = ["rock", "paper", "scissors"]

player_choices = input("Please choose (rock,paper,scissors): ")
if player_choices not in edi_choices:
    print("Invalid. Plese try again")
edi_play = random.choice(edi_choices)
if player_choices == edi_play:
    print(edi_play)
    print("You Both are tie")
elif (player_choices == "rock" and edi_play == "scissors") or \
     (player_choices == "paper" and edi_play == "rock") or \
     (player_choices == "scissors" and edi_play == "paper"):
    print("Winner Winner Chicken Dinner!")
else:
    print("Nah bro! Try again")
print(edi_play)