import random
choices = ["rock", "paper", "scissors"]
print("Rock crushes scissors. Scissors cut paper. Paper covers rock.")
player = input("Do you want to be rock, paper, or scissors (or quit)?")
while player != "quit": # keep playing until the user quits
    player = player.lower() # change user entry to lowercase
    computer = random.choice(choices) #Pick one of the items in choice
    print("You chose " +player+ ", and the computer chose " +computer+".")
    if player == computer:
        print("it's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!!!")
        else:
            print("Computer wins!!")
    elif player == "paper":
        if computer == "rock":
            print("you win!")
        else:
            print("computer wins!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!!")
        else:
            print("Computer wins!!")
    else:
        print("I think it was some sort of error...")
    print() #skip a line
    player = input("Do you want to be rock, paper, or scissors (or quit)?")