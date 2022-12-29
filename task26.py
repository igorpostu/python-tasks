from random import randint

def check_rows(player: int) -> bool:
    for i in range(size):
        win = True
        for j in range(size):
            if game[i][j] != player:
                win = False
                break
        if win:
            return win

def check_columns(player: int) -> bool:
    for i in range(size):
        win = True
        for j in range(size):
            if game[j][i] != player:
                win = False
                break
        if win:
            return win

def check_diagonal_1(player: int) -> bool:
    win = True
    for i in range(size):
        if game[i][i] != player:
            win = False
    if win: return win

def check_diagonal_2(player: int) -> bool:
    win = True
    for i in range(size):
        if game[i][size - 1 - i] != player:
            win = False
            break
    if win: return win

def check_win(player: int) -> bool:
    if check_rows(player) or check_columns(player) or check_diagonal_1(player) or check_diagonal_2(player):
        return True


size = int(input('Enter the board size: '))
game = [[randint(0,2) for i in range(size)] for j in range(size)]
for raw in game:
    print(raw)

if check_win(1):
    print('Player 1 has won!')
elif check_win(2):
    print('Player 2 has won!')
else:
    print('Draw.')