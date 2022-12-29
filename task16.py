from random import randint
import string

words = ['bee', 'tree', 'house', 'fish', 'mama', 'king']
digits = [str(i) for i in range(10)]
lowercase = [string.ascii_lowercase]
uppercase = [string.ascii_uppercase]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

char_dict = {0: digits, 1: lowercase, 2: uppercase, 3: symbols, 4: words}

difficulty = int(input("Difficulty (from 0 to 3): "))

password = ''
if difficulty == 0:
    for i in range(randint(1, 2)):
        password += words[randint(0, len(words) - 1)]
else:
    length = int(input("Length: "))
    for i in range(length):
        key = randint(0, difficulty)
        using_symbols = char_dict[key]
        password += using_symbols[randint(0, len(using_symbols) - 1)]

print('Your password:', password)