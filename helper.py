import pygame

# Box Width
WI = 75

# Defining Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (125, 200, 20)
RED = (255, 0, 0)
BLUE = (10, 100, 255)
GREY = (128, 128, 128)
CYAN = (5, 204, 171)
LGREY = (51, 56, 63)
DARK_GREY = (33, 38, 40)
YELLOW = (255, 217, 0)
ORANGE = (253, 104, 20)
BOXFRONT = (117, 219, 27)
BOXBACK = (17, 119, 45)


def drawO(i, j, k, screen):
    pygame.draw.circle(screen, ORANGE, [50 + WI * i + WI * 3 * k + WI / 2, 50 + WI * j + WI * 3 * k + WI / 2],
                       WI / 3, 10)


def drawX(i, j, k, screen):
    pygame.draw.line(screen, YELLOW, [50 + WI / 4 + WI * i + WI * 3 * k, 50 + WI / 4 + WI * j + WI * 3 * k],
                     [50 - WI / 4 + WI * (i + 1) + WI * 3 * k, 50 - WI / 4 + WI * (j + 1) + WI * 3 * k], 10)
    pygame.draw.line(screen, YELLOW, [50 - WI / 4 + WI * (i + 1) + WI * 3 * k, 50 + WI / 4 + WI * j + WI * 3 * k],
                     [50 + WI / 4 + WI * i + WI * 3 * k, 50 - WI / 4 + WI * (j + 1) + WI * 3 * k], 10)


def drawSelected(i, j, k, screen):
    pygame.draw.line(screen, RED, [50 + WI * i + WI * 3 * k, 50 + WI * j + WI * 3 * k],
                     [50 + WI * (i + 1) + WI * 3 * k, 50 + WI * j + WI * 3 * k], 2)
    pygame.draw.line(screen, RED, [50 + WI * i + WI * 3 * k, 50 + WI * j + WI * 3 * k],
                     [50 + WI * i + WI * 3 * k, 50 + WI * (j + 1) + WI * 3 * k], 2)
    pygame.draw.line(screen, RED, [50 + WI * (i + 1) + WI * 3 * k, 50 + WI * j + WI * 3 * k],
                     [50 + WI * (i + 1) + WI * 3 * k, 50 + WI * (j + 1) + WI * 3 * k], 4)
    pygame.draw.line(screen, RED, [50 + WI * i + WI * 3 * k, 50 + WI * (j + 1) + WI * 3 * k],
                     [50 + WI * (i + 1) + WI * 3 * k, 50 + WI * (j + 1) + WI * 3 * k], 4)


def update(screen, board):
    screen.fill(DARK_GREY)
    for i in range(3):
        pygame.draw.line(screen, BOXFRONT, [50 + 3 * WI * i, 50 + 3 * WI * i],
                         [50 + 3 * WI * i, 50 + 3 * WI * i + 3 * WI], 1)
        pygame.draw.line(screen, BOXFRONT, [50 + 3 * WI * i, 50 + 3 * WI * i],
                         [50 + 3 * WI * i + 3 * WI, 50 + 3 * WI * i], 1)
        pygame.draw.line(screen, BOXFRONT, [50 + 3 * WI * i + 3 * WI, 50 + 3 * WI * i + 3 * WI],
                         [50 + 3 * WI * i, 50 + 3 * WI * i + 3 * WI], 4)
        pygame.draw.line(screen, BOXFRONT, [50 + 3 * WI * i + 3 * WI, 50 + 3 * WI * i + 3 * WI],
                         [50 + 3 * WI * i + 3 * WI, 50 + 3 * WI * i], 4)
        for j in range(2):
            pygame.draw.line(screen, CYAN, [50 + (j + 1) * WI + 3 * WI * i, 50 + 3 * WI * i],
                             [50 + (j + 1) * WI + 3 * WI * i, 50 + 3 * WI * i + 3 * WI], 10)
            pygame.draw.line(screen, CYAN, [50 + 3 * WI * i, 50 + (j + 1) * WI + 3 * WI * i],
                             [50 + 3 * WI * i + 3 * WI, 50 + (j + 1) * WI + 3 * WI * i], 10)

    pygame.draw.line(screen, RED, [50, 275], [500, 725], 2)
    pygame.draw.line(screen, RED, [275, 50], [725, 500], 2)
    # pygame.draw.line(screen, RED, [275, 275], [725, 725], 2)

    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                if board.board[i][j][k] == 1:
                    drawX(i, j, k, screen)
                elif board.board[i][j][k] == 2:
                    drawO(i, j, k, screen)


def getPoints(event):
    x = ((event.pos[0] - 50) // WI) % 3
    y = ((event.pos[1] - 50) // WI) % 3
    z = ((event.pos[0] - 50) // WI) // 3

    if int(int(int(event.pos[0] - 50) / WI) / 3) != int(int(int(event.pos[1] - 50) / WI) / 3):
        z = -1

    return x, y, z


def format_time(secs):
    secs = int(secs)
    sec = secs % 60
    minute = secs // 60

    s = str(sec)
    m = str(minute)

    if len(s) == 1:
        s = '0' + s

    if len(m) == 1:
        m = '0' + m

    mat = " " + m + ":" + s
    return mat
