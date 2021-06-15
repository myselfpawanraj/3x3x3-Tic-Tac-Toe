import subprocess
from sys import platform


class Board:

    def __init__(self):
        self.matrix = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

    def findMax(self):
        index = [-1, -1, -1]

        # Print Matrix
        boardString = ''
        out = ''

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    boardString += (' ' + str(self.matrix[i][j][k]))

        print(boardString)

        # Run cpp file

        if platform == "linux" or platform == "linux2":
            out = subprocess.run(["./cpp_executables/Programme"], text=True, input=boardString,
                                 stdout=subprocess.PIPE).stdout
        elif platform == "darwin":
            out = subprocess.run(["./cpp_executables/Programme"], text=True, input=boardString,
                                 stdout=subprocess.PIPE).stdout
        elif platform == "win32":
            out = subprocess.run(["./cpp_executables/Programme.exe"], text=True, input=boardString,
                                 stdout=subprocess.PIPE).stdout

        # Take input

        out = out.splitlines()
        index[0] = int(out[0])
        index[1] = int(out[1])
        index[2] = int(out[2])

        print(out)

        return index

    def isEmpty(self):
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    if self.matrix[i][j][k] == 0:
                        return True
        return False

    def isWin(self, val):

        # To check diagonal lines of the cube

        if self.matrix[0][0][0] == val & self.matrix[1][1][1] == val & self.matrix[2][2][2] == val:
            return True

        if self.matrix[0][0][2] == val & self.matrix[1][1][1] == val & self.matrix[2][2][0] == val:
            return True

        if self.matrix[2][0][0] == val & self.matrix[1][1][1] == val & self.matrix[0][2][2] == val:
            return True

        if self.matrix[2][0][2] == val & self.matrix[1][1][1] == val & self.matrix[0][2][0] == val:
            return True

        # To check straight lines

        poss = False
        for i in range(0, 3):
            for j in range(0, 3):

                temp = True
                for k in range(0, 3):
                    if self.matrix[i][j][k] != val:
                        temp = False
                poss |= temp

                temp = True
                for k in range(0, 3):
                    if self.matrix[i][k][j] != val:
                        temp = False
                poss |= temp

                temp = True
                for k in range(0, 3):
                    if self.matrix[k][i][j] != val:
                        temp = False
                poss |= temp

        # To check 2D Diagonal lines

        for i in range(0, 3):
            if self.matrix[0][0][i] == val & self.matrix[1][1][i] == val & self.matrix[2][2][i] == val:
                return True

            if self.matrix[2][0][i] == val & self.matrix[1][1][i] == val & self.matrix[0][2][i] == val:
                return True

            if self.matrix[0][i][0] == val & self.matrix[1][i][1] == val & self.matrix[2][i][2] == val:
                return True

            if self.matrix[2][i][0] == val & self.matrix[1][i][1] == val & self.matrix[0][i][2] == val:
                return True

            if self.matrix[i][0][0] == val & self.matrix[i][1][1] == val & self.matrix[i][2][2] == val:
                return True

            if self.matrix[i][2][0] == val & self.matrix[i][1][1] == val & self.matrix[i][0][2] == val:
                return True

        return poss

    def printBoard(self):
        for i in range(0, 3):
            print('Board : ' + str(i + 1))
            print('-------')
            for j in range(0, 3):
                print('|', end='')
                for k in range(0, 3):
                    if self.matrix[i][j][k] == 0:
                        print(' ', end='|')
                    elif self.matrix[i][j][k] == 1:
                        print('X', end='|')
                    else:
                        print('O', end='|')

                print()
                print('-------')

            print()
            print()
