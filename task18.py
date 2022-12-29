from random import randint

def check(num1: str, num2: str) -> bool:
    global cows, bulls
    if num1 == num2:
        return True
    for i in range(len(num1)):
        if num1[i] == num2[i]:
            cows += 1
        elif num1[i] in num2:
            bulls += 1
    return False


comp_num = str(randint(1000, 9999))

guess_counter = 0
user_num = "0000"
while True:
    guess_counter += 1
    if user_num == comp_num:
        print("This is right! You took", guess_counter, "guesses")
        break
    cows = 0
    bulls = 0
    user_num = input("Enter a 4-digit number: ")
    check(user_num, comp_num)
    print(cows, "cows,", bulls, "bulls")
