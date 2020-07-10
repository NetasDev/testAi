import chessLogic as cl
import random

#test movements of:
#pawn
"""
board = cl.Board()
board.print_board()
print(board.get_all_moves(1))
board.make_move(((1,0),(3,0)))
board.print_board()
"""
dictionary = {
  "a": 1,
  "b": 2,
  "c": 3,
  "d": 4,
  "e": 5,
  "f": 6,
  "g": 7,
  "h": 8
}

board = cl.Board()
player = 1
turns = 0

while(True):
    turns = turns+1
    print("player to move: ",end="")
    print(player)
    board.print_board()
    moves = board.get_all_moves(player)
    print(moves)
    #print("Make a move:")
    if len(moves) == 0:
      board.print_board()
      print("unable to move")
      print(player)
      break
    number = random.randrange(len(moves))
    print(moves[number])
    board.make_move(moves[number])
    print(board.turns_without_action)
    if board.turns_without_action >= 40:
      print(turns)
      print("40 züge ohne aktion")
      break
    player = player*-1
    """
    while(True):    
        var = input()
        if(len(var)>=4):
            move =  ((int(var[0]),int(var[1])),(int(var[2]),int(var[3])))
            if move in moves:
                print("legal move done")
                board.make_move(move)
                player = player * -1
                break
    """
            

        

            

    
