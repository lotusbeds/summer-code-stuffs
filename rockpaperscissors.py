import random

#0 is rock
#1 is paper
#2 is scissors

def play():
    while True:
        computer = random.randint(0, 2)
        player = input("Let's play rock-paper-scissors!! Type in 'rock' 'paper' or 'scissors'")
        if((computer == 0) and (player == "rock")):
            print("The computer said: rock")
            print("You said: rock")
            print("Tie!! Try again!!")
        elif((computer == 0) and (player == "paper")):
            print("The computer said: rock")
            print("You said: paper")
            print("You win!!")
        elif((computer == 0) and (player == "scissors")):
            print("The computer said: rock")
            print("You said: scissors")
            print("You lose!! Try again!!")
        elif((computer == 1) and (player == "rock")):
            print("The computer said: paper")
            print("You said: rock")
            print("You lose!! Try again!!")
        elif((computer == 1) and (player == "paper")):
            print("The computer said: paper")
            print("You said: paper")
            print("Tie!! Try again!!")
        elif((computer == 1) and (player == "scissors")):
            print("The computer said: paper")
            print("You said: scissors")
            print("You win!!")
        elif((computer == 2) and (player == "rock")):
            print("The computer said: scissors")
            print("You said: rock")
            print("You win!!")
        elif((computer == 2) and (player == "paper")):
            print("The computer said: scissors")
            print("You said: paper")
            print("You lose!! Try again!!")
        elif((computer == 2) and (player == "scissors")):
            print("The computer said: scissors")
            print("You said: scissors")
            print("Tie!! Try again!!")
        elif player == "stop" or player == "end":
            print("Ok!! We can take a break")
            break
        else:
            print("Please enter 'rock' 'paper' or 'scissors'.")

play()