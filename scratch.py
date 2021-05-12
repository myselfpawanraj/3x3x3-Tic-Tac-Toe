import subprocess

board = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[10,11,12],[13,14,15],[16,17,18]],
    [[19,20,21],[22,23,24],[25,26,27]]
]

i = 0
for i in range(3):
    boardString = [' '.join([str(c) for c in lst]) for lst in board[i]]
boardString = ' '.join(boardString)
    
out = subprocess.run(["./MiniMax"], text=True, input=boardString, stdout=subprocess.PIPE).stdout
print(out.splitlines())
