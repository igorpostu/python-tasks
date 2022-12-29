p1 = input("Player 1 choice: ")
p2 = input("Player 2 choice: ")

if p1 == p2:
    print("It's a draw")
elif p1 == "rock":
    if p2 == "paper":
        print("Player 2 wins")
    else:
        print("Player 1 wins")
elif p1 == "paper":
    if p2 == "scissors":
        print("Player 2 wins")
    else:
        print("Player 1 wins")
elif p1 == "scissors":
    if p2 == "rock":
        print("Player 2 wins")
    else:
        print("Player 1 wins")
