import numpy
board = numpy.zeros((8,8))


def fill_board(board):
    #Representation of Chess pieces as Numbers:
    #Pawn = 1;King = 2;Queen = 3;Bishop = 4;Knight = 5;Rook = 6; Leer = 0
    #Negative Numbers = Black Piece
    board[0][0]=board[0][7] = 6
    board[0][1]=board[0][6] = 5
    board[0][2]=board[0][5] = 4
    board[0][3] = 2
    board[0][4] = 3
    for i in range(8):
        board[1][i] = 1
        board[6][i] = -1
        board[7][7-i] = -board[0][i]
    return board



board = fill_board(board)
print(board)


