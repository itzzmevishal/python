from random import randint

t=["Rock", "Paper", "Scissor"]
computer=t[randint(0,2)]
player=False

while player == False:
   
    player= input("Rock,Paper,Scissors \n")
    if player == computer:
        print("Tie")
    elif player == "Rock" or "R" or "rock":
        if computer == "Paper":
            print("You Lose", computer, "covers", player)
        else:
            print("You win", player, "smashes", computer)
    elif player == "Paper" or "P" or "paper":
        if computer == "Scissors":
            print("You lose", computer,"cut", player)
        else:
            print("You Win", player, "covers",computer)
    elif player == "Scissors" or "S" or "scissors":
        if computer == "Rock":
            print("You Lose", computer, "smashes", player)
        else:
            print("You Win", player, "cut", computer)
    else:
        print("Thats not a valid play, See your Spelling ")
    play_again=input("Do You want to play??? Y or N \n")
    if play_again == "N" or "n":
        break 
   
    player = False
    computer = t[randint(0,2)] 
