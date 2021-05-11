from Board import Board
from helper import WI
import helper
import MiniMax
import pygame

board = Board()
pygame.init()
size = (775, 775)
screen = pygame.display.set_mode(size)


def initialise():
    global board
    global screen
    board = Board()


playing = True
x, y, z = (-1, -1, -1)
turn = 1
initialise()

while playing:
    helper.update(screen, board)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.MOUSEMOTION:
            x, y, z = helper.getPoints(event)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (0 <= x <= 2) & (0 <= y <= 2) & (0 <= z <= 2):
                    if board.board[x][y][z] == 0 and turn == 1:
                        board.board[x][y][z] = 1
                        turn = 2
            elif event.button == 3:
                if not board.isSpace():
                    initialise()
                    turn = 0

    if (0 <= x <= 2) & (0 <= y <= 2) & (0 <= z <= 2):
        print(str(x) + str(y) + str(z))
        helper.drawSelected(x, y, z, screen)

    # x = 0  # int(input('input x '))
    # y = 0  # int(input('input y '))
    # z = 0  # int(input('input z '))
    #
    # board.board[z][y][x] = 1

    # if board.isWin(1):
    #     print('User Won!')
    #     break
    #
    # if not board.isSpace():
    #     print('Draw Occurred!')
    #     break

    if turn == 2:
        a, b, c = MiniMax.findMax(board.board)
        board.board[a][b][c] = 2
        turn = 1
    # board.viewBoard()

    # if not board.isSpace():
    #     print('Draw Occurred!')
    #     break
    #
    # if board.isWin(2):
    #     print('CPU Won!')
    #     break
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
