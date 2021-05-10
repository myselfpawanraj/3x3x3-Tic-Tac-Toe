from Board import Board
import random

# board = [[[2, 1, 2], [0, 1, 2], [1, 1, 2]],
#          [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
#          [[2, 1, 2], [1, 1, 2], [0, 1, 2]]]

# board = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
#          [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
#          [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]


board = Board()

while board.isSpace():
    x = int(input('input x '))
    y = int(input('input y '))
    z = int(input('input z '))

    board.board[x][y][z] = 1

    if board.isWin(1):
        print('User Won!')
        break

    if not board.isSpace():
        print('Draw Occurred!')
        break

    x = random.randint(0, 2)
    y = random.randint(0, 2)
    z = random.randint(0, 2)

    while board.board[x][y][z] != 0:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        z = random.randint(0, 2)

    board.board[x][y][z] = 2
    board.viewBoard()

    if not board.isSpace():
        print('Draw Occurred!')
        break

    if board.isWin(2):
        print('CPU Won!')
        break
