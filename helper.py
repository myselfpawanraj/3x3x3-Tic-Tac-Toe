import pygame

# Defining Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LGREY = (239, 239, 239)
GREEN = (0, 255, 0)
LIGHT_GREEN = (125, 200, 20)
RED = (255, 0, 0)
BLUE = (10, 100, 255)
GREY = (128, 128, 128)

WI = 75


def drawO(i, j, k, screen):
    pygame.draw.circle(screen, GREEN, [50 + WI * i + WI * 3 * k + WI / 2, 50 + WI * j + WI * 3 * k + WI / 2],
                       WI / 4, 2)


def drawX(i, j, k, screen):
    pygame.draw.line(screen, BLUE, [50 + WI / 4 + WI * i + WI * 3 * k, 50 + WI / 4 + WI * j + WI * 3 * k],
                     [50 - WI / 4 + WI * (i + 1) + WI * 3 * k, 50 - WI / 4 + WI * (j + 1) + WI * 3 * k], 4)
    pygame.draw.line(screen, BLUE, [50 - WI / 4 + WI * (i + 1) + WI * 3 * k, 50 + WI / 4 + WI * j + WI * 3 * k],
                     [50 + WI / 4 + WI * i + WI * 3 * k, 50 - WI / 4 + WI * (j + 1) + WI * 3 * k], 4)


def drawSelected(i, j, k, screen):
    pygame.draw.line(screen, RED, [50 + WI * i + WI * 3 * k, 50 + WI * j + WI * 3 * k],
                     [50 + WI * (i + 1) + WI * 3 * k, 50 + WI * j + WI * 3 * k], 2)
    pygame.draw.line(screen, RED, [50 + WI * i + WI * 3 * k, 50 + WI * j + WI * 3 * k],
                     [50 + WI * i + WI * 3 * k, 50 + WI * (j + 1) + WI * 3 * k], 2)
    pygame.draw.line(screen, RED, [50 + WI * (i + 1) + WI * 3 * k, 50 + WI * j + WI * 3 * k],
                     [50 + WI * (i + 1) + WI * 3 * k, 50 + WI * (j + 1) + WI * 3 * k], 2)
    pygame.draw.line(screen, RED, [50 + WI * i + WI * 3 * k, 50 + WI * (j + 1) + WI * 3 * k],
                     [50 + WI * (i + 1) + WI * 3 * k, 50 + WI * (j + 1) + WI * 3 * k], 2)


def update(screen, board):
    screen.fill(LGREY)
    for i in range(3):
        pygame.draw.line(screen, BLACK, [50 + 3 * WI * i, 50 + 3 * WI * i],
                         [50 + 3 * WI * i, 50 + 3 * WI * i + 3 * WI], 2)
        pygame.draw.line(screen, BLACK, [50 + 3 * WI * i, 50 + 3 * WI * i],
                         [50 + 3 * WI * i + 3 * WI, 50 + 3 * WI * i], 2)
        pygame.draw.line(screen, BLACK, [50 + 3 * WI * i + 3 * WI, 50 + 3 * WI * i + 3 * WI],
                         [50 + 3 * WI * i, 50 + 3 * WI * i + 3 * WI], 2)
        pygame.draw.line(screen, BLACK, [50 + 3 * WI * i + 3 * WI, 50 + 3 * WI * i + 3 * WI],
                         [50 + 3 * WI * i + 3 * WI, 50 + 3 * WI * i], 2)
        for j in range(2):
            pygame.draw.line(screen, BLACK, [50 + (j + 1) * WI + 3 * WI * i, 50 + 3 * WI * i],
                             [50 + (j + 1) * WI + 3 * WI * i, 50 + 3 * WI * i + 3 * WI], 1)
            pygame.draw.line(screen, BLACK, [50 + 3 * WI * i, 50 + (j + 1) * WI + 3 * WI * i],
                             [50 + 3 * WI * i + 3 * WI, 50 + (j + 1) * WI + 3 * WI * i], 1)

    pygame.draw.line(screen, GREY, [50, 275], [500, 725], 1)
    pygame.draw.line(screen, GREY, [275, 50], [725, 500], 1)
    pygame.draw.line(screen, GREY, [275, 275], [725, 725], 1)

    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                if board.board[i][j][k] == 1:
                    drawX(i, j, k, screen)
                elif board.board[i][j][k] == 2:
                    drawO(i, j, k, screen)


def getPoints(event):
    x = int(int(int(event.pos[0] - 50) / WI) % 3)
    y = int(int(int(event.pos[1] - 50) / WI) % 3)
    z = int(int(int(event.pos[0] - 50) / WI) / 3)
    return x, y, z
