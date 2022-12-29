def draw_board(size: int) -> None:
    for i in range(size):
        print('--- ' * size)
        print('| ' * (2*size))
    print('--- ' * size)


size = int(input('Enter the size of the board: '))

draw_board(size)