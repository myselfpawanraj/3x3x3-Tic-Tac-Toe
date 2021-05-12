from Board import Board
import helper
import MiniMax
import pygame
import time

board = Board()
pygame.init()
pygame.display.set_caption("3x3x3 TTT ~ by Pawan Raj")
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
size = (775, 775)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("comicsans", 40)
start = time.time()

me = 0
you = 0
turn = 1
playing = True
x, y, z = (-1, -1, -1)

while playing:
    helper.update(screen, board)
    play_time = int(round(time.time() - start))
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
                        if board.isWin(1):
                            you += 1
                        turn = 2
            elif event.button == 3:
                if (not board.isSpace()) | board.isWin(1) | board.isWin(2):
                    board = Board()
                    turn = 1

    if (0 <= x <= 2) & (0 <= y <= 2) & (0 <= z <= 2):
        # print(str(x) + str(y) + str(z))
        helper.drawSelected(x, y, z, screen)

    if board.isWin(1):
        text = font.render(' You have won the game ! Right Click to Restart ', True, helper.YELLOW, helper.LGREY)
        textRect = text.get_rect()
        textRect.center = (775/2, 25)
        screen.blit(text, textRect)
        turn = 0

    elif turn == 2:
        a, b, c = MiniMax.findMax(board.board)
        if (0 <= a <= 2) & (0 <= b <= 2) & (0 <= c <= 2):
            board.board[a][b][c] = 2
            if board.isWin(2):
                me += 1
        turn = 1

    elif not board.isSpace():
        text = font.render(' Draw , Right Click to Restart', True, helper.LGREY, helper.LGREY)
        textRect = text.get_rect()
        textRect.center = (775/2, 25)
        screen.blit(text, textRect)
        turn = 0

    if board.isWin(2):
        text = font.render(' Bot has won the game ! Right Click to Restart ', True, helper.ORANGE, helper.LGREY)
        textRect = text.get_rect()
        textRect.center = (775/2, 25)
        screen.blit(text, textRect)
        turn = 0

    screen.blit(font.render(" Time: " + helper.format_time(play_time),
                            True, helper.GREY), (550, 740))

    screen.blit(font.render(" You: " + str(you) + "   Bot: " + str(me) + ' ',
                            True, helper.GREY), (50, 740))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
