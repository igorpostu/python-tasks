from random import randint

def pick_random() -> str:
    with open('task30_sowpods.txt', 'r') as f:
        lines = f.readlines()
        return lines[randint(0, len(lines))].strip()

def insert(letter: str, correct_letters: list, word: list) -> None:
    for i in range(len(word)):
            if letter == word[i]:
                correct_letters[i] = word[i]

def list_print(A: list) -> None:
    for elem in A:
        print(elem, end='')
    print()

word = list(pick_random())
correct_letters = list('_' * len(word))
list_print(correct_letters)

guessed_letters = []
while correct_letters != word:
    letter = input('Guess a letter: ').upper()
    if letter in guessed_letters:
        print('You already have guessed that letter!')
    elif letter in word:
        insert(letter, correct_letters, word)
        list_print(correct_letters)
    else:
        print('Incorrect!')
    guessed_letters.append(letter)
else:
    print('Congratulations!')