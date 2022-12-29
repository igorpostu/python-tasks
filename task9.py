import random

num = random.randint(1, 9)
guess_count = 0

while True:
    guess = input("Guess a number or type \"exit\": ")
    guess_count += 1
    if guess == "exit":
        break
    if int(guess) < num:
        print("Too low!")
    elif int(guess) > num:
        print("Too high!")
    else:
        print("This is the right number! You have taken", guess_count, "guesses.")
        num = random.randint(1, 9)
        guess_count = 0