class Board:

    def __init__(self):
        self.board = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

    def isSpace(self):
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    if self.board[i][j][k] == 0:
                        return True
        return False

    def winner(self):
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    if self.board[i][j][k] == 0:
                        return True
        return False

    def viewBoard(self):
        for i in range(0, 3):
            print('Board : ' + str(i + 1))
            print('-------')
            for j in range(0, 3):
                print('|', end='')
                for k in range(0, 3):
                    if self.board[i][j][k] == 0:
                        print(' ', end='|')
                    elif self.board[i][j][k] == 1:
                        print('X', end='|')
                    else:
                        print('O', end='|')

                print()
                print('-------')

            print()
            print()

    def isWin(self, val):
        poss = False
        for i in range(0, 3):
            for j in range(0, 3):

                # To check straight lines

                temp = True
                for k in range(0, 3):
                    if self.board[i][j][k] != val:
                        temp = False
                poss |= temp

                temp = True
                for k in range(0, 3):
                    if self.board[i][k][j] != val:
                        temp = False
                poss |= temp

                temp = True
                for k in range(0, 3):
                    if self.board[k][i][j] != val:
                        temp = False
                poss |= temp

                # To check diagonal lines of the cube

                if self.board[0][0][0] == val & self.board[1][1][1] == val & self.board[2][2][2] == val:
                    return True

                if self.board[0][0][2] == val & self.board[1][1][1] == val & self.board[2][2][0] == val:
                    return True

                if self.board[2][0][0] == val & self.board[1][1][1] == val & self.board[0][2][2] == val:
                    return True

                if self.board[2][0][2] == val & self.board[1][1][1] == val & self.board[0][2][0] == val:
                    return True

        return poss
