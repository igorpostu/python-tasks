number = int(input("Enter a number: "))
check = int(input("Enter a check: "))

if number % 4 == 0:
    print("Number", number, "is even and is multiple of 4")
elif number % 2 == 0:
    print("Number", number, "is even")
else:
    print("Number", number, "is odd")

if number % check == 0:
    print("Number", number, "divides by", check, "evenly")
else:
    print("Number", number, "does not divide by", check, "evenly")
