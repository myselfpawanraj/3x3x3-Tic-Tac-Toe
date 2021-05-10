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
        print()
