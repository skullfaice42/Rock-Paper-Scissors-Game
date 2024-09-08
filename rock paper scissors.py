import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = (None)




    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()


    if computer == player:
        print ("Computer chose" + computer)
        print ("Player chose" + player)
        print ("Tie!")

    elif player == "rock":
        if computer == "scissors":
            print ("Player chose" + player)
            print ("Computer chose" + computer)
            print ("You Win!")
        if computer == "paper":
            print ("Player chose" + player)
            print ("Computer chose" + computer)
            print ("You Lose!")

    elif player == "paper":
        if computer == "scissors":
            print ("Player chose" + player)
            print ("Computer chose" + computer)
            print ("You Lose!")
        if computer == "rock":
            print ("Player chose" + player)
            print ("Computer chose" + computer)
            print ("You Win!")

    elif player == "scissors":
        if computer == "rock":
            print ("Player chose" + player)
            print ("Computer chose" + computer)
            print ("You Lose!")
        if computer == "paper":
            print ("Player chose" + player)
            print ("Computer chose" + computer)
            print ("You Win!")

    going_again = input ("Wanna go again? yes/no: ").lower()
    if going_again != "yes":
        break

print("Cya")