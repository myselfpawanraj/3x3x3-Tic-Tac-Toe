import subprocess
from sys import platform


def findMax(board):
    index = [-1, -1, -1]

    # Print Matrix
    boardString = ''
    out = ''

    for i in range(3):
        for j in range(3):
            for k in range(3):
                boardString += (' ' + str(board[i][j][k]))

    print(boardString)

    # Run cpp file

    if platform == "linux" or platform == "linux2":
        out = subprocess.run(["./CPP_Executables/Programme"], text=True, input=boardString, stdout=subprocess.PIPE).stdout
    elif platform == "darwin":
        out = subprocess.run(["./CPP_Executables/Programme"], text=True, input=boardString, stdout=subprocess.PIPE).stdout
    elif platform == "win32":
        out = subprocess.run(["./CPP_Executables/Programme.exe"], text=True, input=boardString, stdout=subprocess.PIPE).stdout

    # Take input

    out = out.splitlines()
    index[0] = int(out[0])
    index[1] = int(out[1])
    index[2] = int(out[2])

    print(out)

    return index


# At first I tried to code MINIMAX in Python but its too slow,
# So I replaced it with a CPP code
# Below is the previous implementation

'''
def findMax(board):
    val = -2
    index = (-1, -1, -1)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if board[i][j][k] == 0:
                    board[i][j][k] = 2
                    t = miniMax(board, 1, 0)
                    board[i][j][k] = 0
                    if t > val:
                        val = t
                        index = (i, j, k)
                    if val == 1:
                        return index
    return index


def miniMax(board, turn, depth):
    # print(turn)
    # viewBoard(board)

    if isWin(board, 2):
        return 1
    if isComplete(board):
        return 0
    if isWin(board, 1):
        return -1

    if depth >= 2:
        return 0

    if turn == 1:
        val = 2
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if board[i][j][k] == 0:
                        board[i][j][k] = turn
                        t = miniMax(board, turn % 2 + 1, depth + 1)
                        board[i][j][k] = 0
                        if t < val:
                            val = t
                        if val == -1:
                            return val
        return val

    else:
        val = -2
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if board[i][j][k] == 0:
                        board[i][j][k] = turn
                        t = miniMax(board, turn % 2 + 1, depth + 1)
                        board[i][j][k] = 0
                        if t > val:
                            val = t
                        if val == 1:
                            return val
        return val


def isWin(board, val):
    # To check diagonal lines of the cube

    if board[0][0][0] == val & board[1][1][1] == val & board[2][2][2] == val:
        return True

    if board[0][0][2] == val & board[1][1][1] == val & board[2][2][0] == val:
        return True

    if board[2][0][0] == val & board[1][1][1] == val & board[0][2][2] == val:
        return True

    if board[2][0][2] == val & board[1][1][1] == val & board[0][2][0] == val:
        return True

    # To check straight lines

    poss = False
    for i in range(0, 3):
        for j in range(0, 3):

            temp = True
            for k in range(0, 3):
                if board[i][j][k] != val:
                    temp = False
            poss |= temp

            temp = True
            for k in range(0, 3):
                if board[i][k][j] != val:
                    temp = False
            poss |= temp

            temp = True
            for k in range(0, 3):
                if board[k][i][j] != val:
                    temp = False
            poss |= temp

    # To check 2D Diagonal lines

    for i in range(0, 3):
        if board[0][0][i] == val & board[1][1][i] == val & board[2][2][i] == val:
            return True

        if board[2][0][i] == val & board[1][1][i] == val & board[0][2][i] == val:
            return True

        if board[0][i][0] == val & board[1][i][1] == val & board[2][i][2] == val:
            return True

        if board[2][i][0] == val & board[1][i][1] == val & board[0][i][2] == val:
            return True

        if board[i][0][0] == val & board[i][1][1] == val & board[i][2][2] == val:
            return True

        if board[i][2][0] == val & board[i][1][1] == val & board[i][0][2] == val:
            return True

    return poss


def isComplete(board):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if board[i][j][k] == 0:
                    return False

    return True


def viewBoard(board):
    for i in range(0, 3):
        print('Board : ' + str(i + 1))
        print('-------')
        for j in range(0, 3):
            print('|', end='')
            for k in range(0, 3):
                if board[i][j][k] == 0:
                    print(' ', end='|')
                elif board[i][j][k] == 1:
                    print('X', end='|')
                else:
                    print('O', end='|')

            print()
            print('-------')

        print()
        print() '''
