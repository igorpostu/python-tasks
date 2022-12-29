from random import randint

def pick_random(file) -> str:
    lines = file.readlines()
    return lines[randint(0, len(lines))].strip()

with open('task30_sowpods.txt', 'r') as f:
    print(pick_random(f))