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

def player_move(player: int) -> None:
    print('Player', player, 'move')
    raw = int(input('raw = ')) - 1
    col = int(input('col = ')) - 1
    while game[raw][col] != 0:
        print('This cell is taken! Choose empty one.')
        raw = int(input('raw = ')) - 1
        col = int(input('col = ')) - 1
    game[raw][col] = player
    print_game(game)

def print_game(game: list) -> None:
    for elem in game:
        print(elem)


p1 = 0
p2 = 0
answer = 'yes'
while answer == 'yes':
    size = int(input('Enter the game size: '))
    game = [[0 for i in range(size)] for j in range(size)]
    print_game(game)

    player = 2
    turn = 1
    free_cells = size ** 2

    while free_cells != 0:
        turn *= -1
        player += turn
        player_move(player)
        free_cells -= 1
        
        if check_win(1):
            print('Player 1 has won!')
            p1 += 1
            break
        if check_win(2):
            print('Player 2 has won!')
            p2 += 1
            break
        if free_cells == 0:
            print('It\'s a draw.')
    print('Player 1:', p1, '\nPlayer 2:', p2)

    answer = input('Do you want to play again?\nAnswer: ')