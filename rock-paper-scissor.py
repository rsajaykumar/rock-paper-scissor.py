#importing random module
import random
# Game Loop
while True:
    choices = ['rock', 'paper', 'scissor']
    
    computer = random.choice(choices)
    player = None
    
    while player not in choices:
        player = input("rock, paper, or scissor: ").lower()
        
    if player == computer:
        print("Computer: ",computer)
        print("Player: ",player)
        print("TIE")
        
    elif player == "rock":
        if computer == "scissor":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Win")
        
    elif player == "scissor":
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Lose")
        
    elif player == "paper":
        if computer == "scissor":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Lose")
        
    elif player == "scissor":
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Win")
        
    elif player == "paper":
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Lose")
            
