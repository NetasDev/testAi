import numpy as np
import copy
class Piece():
    def __init__(self,player):
        self.player = player
        self.abreviation = ""
        self.index = 100

    def get_abreviation(self):
        return self.abreviation

    def get_player(self):
        return self.player
    
    def get_index(self):
        return self.index

    def repeat_motion(self,board,motions,x,y):
        moves = []
        for addx,addy in motions:
            xnew,ynew = x+addx,y+addy
            while xnew<8 and xnew >0 and ynew<8 and ynew>0:
                field = board.pos[xnew][ynew]
                if field.get_index() == 0:
                    moves.append(((x,y),(xnew,ynew)))
                    
                elif field.player != self.player:
                    moves.append(((x,y),(xnew,ynew)))
                    break
                else:
                    break
                xnew,ynew = xnew+addx,ynew+addy
        return moves
                

    
    def get_moves(self,Board,x,y):
        print("no moves")
        

        
class Pawn(Piece):
    def __init__(self,player):
        super().__init__(player)
        self.moved = False
        self.abreviation = "P"
        self.index = 1
        
    def get_moves(self,Board,x,y):
        moves = []
        x1 = x+self.player*1
        x2 = x+self.player*2
        if x1 <7 and x1>0:
            if Board.pos[x1][y].get_index() == 0:
                moves.append(((x,y),(x1,y)))
        if x1 <=7 and x1>=0 and x2<7 and x2>0:
            if Board.pos[x1][y].get_index() == 0 and Board.pos[x2][y].get_index() == 0 and self.moved == False:
                moves.append(((x,y),(x2,y)))
        if y<=6 and x<6 and x>1:
            if Board.pos[x+1*self.player][y+1].get_player() == self.player*-1:
                moves.append(((x,y),(x+1*self.player,y+1)))
        if y>=1 and x<6 and x>1:
            if Board.pos[x+1*self.player][y-1].get_player() == self.player*-1:
                moves.append(((x,y),(x+1*self.player,y-1)))

        if self.player == -1 and x == 1:
            if Board.pos[0][y].get_index()==0:
                for i in (3,4,5,6):
                    moves.append(((x,y),(0,y,i)))
            if y<=6:
                if Board.pos[0][y+1].get_player() == self.player*-1:
                    for i in (3,4,5,6):
                        moves.append(((x,y),(0,y+1,i)))
            if y>=1:
                if Board.pos[0][y-1].get_player() == self.player*-1:
                    for i in (3,4,5,6):
                        moves.append(((x,y),(0,y-1,i)))

        if self.player == 1 and x == 6:
            if Board.pos[7][y].get_index()==0:
                for i in (3,4,5,6):
                    moves.append(((x,y),(7,y,i)))
            if y<=6:
                if Board.pos[7][y+1].get_player() == self.player*-1:
                    for i in (3,4,5,6):
                        moves.append(((x,y),(7,y+1,i)))
            if y>=1:
                if Board.pos[7][y-1].get_player() == self.player*-1:
                    for i in (3,4,5,6):
                        moves.append(((x,y),(7,y-1,i)))
        
        

        return moves
    ###

    
class King(Piece):
    def __init__(self,player):
        super().__init__(player)
        self.abreviation = "K"
        self.moved = False
        self.index = 2

    def get_moves(self,Board,x,y):
        moves = []
        options = [(x+1,y+1),(x+1,y),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1)]
        
        for entry in options:
            if entry[0]>=0 and entry[0]<=7 and entry[1]>=0 and entry[1]<=7:
                moves.append(((x,y),(entry[0],entry[1])))
        """
                tempboard=copy.deepcopy(Board)
                tempboard.make_move(((x,y),(entry[0],entry[1])))
                if tempboard.check_for_check(self.player) == False:
                    moves.append(((x,y),(entry[0],entry[1])))
        """
        return moves

        

class Queen(Piece):
    def __init__(self,player):
        super().__init__(player)
        self.abreviation = "Q"
        self.index = 3
    
    def get_moves(self,Board,x,y):
        motions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        return self.repeat_motion(Board,motions,x,y)

class Knight(Piece):
    def __init__(self,player):
        super().__init__(player)
        self.abreviation = "N"
        self.index = 4
    
    def get_moves(self,Board,x,y):
        moves = []
        options = [(x+2,y+1),(x+2,y-1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2),(x-2,y+1),(x-2,y-1)]
        for entry in options:
            if entry[0]>=0 and entry[1]>=0 and entry[0]<=7 and entry[1] <=7 and Board.pos[entry[0]][entry[1]].get_player()!=self.get_player():
                moves.append(((x,y),entry))
        return moves

class Bishop(Piece):
    def __init__(self,player):
        super().__init__(player)
        self.abreviation = "B"
        self.index = 5
    
    def get_moves(self,Board,x,y):
        motions = [(1,1),(1,-1),(-1,1),(-1,-1)]
        return self.repeat_motion(Board,motions,x,y)
        

class Rook(Piece):
    def __init__(self,player):
        super().__init__(player)
        self.abreviation = "R"
        self.index = 6
    
    def get_moves(self,Board,x,y):
        motions = [(1,0),(0,1),(-1,0),(0,-1)]
        return self.repeat_motion(Board,motions,x,y)

class Empty(Piece):
    def __init__(self):
        self.player = 0
        self.isEmpty = True
        self.abreviation = "-"
        self.index = 0

    def get_moves(self,Board,x,y):
        return 



class Board():
    def __init__(self):
        self.turns_without_action = 0
        self.whitepieces = []
        self.blackpieces = []
        self.pos = np.full((8,8), Empty())
        #Representation of Chess pieces as Numbers:
        #Pawn = 1;King = 2;Queen = 3;Knight = 5;Bishop = 4;Rook = 6; Leer = 0
        #Negative Numbers = Black Piece

        for i in range(8):
            self.pos[1][i] = Pawn(1,)
            self.pos[6][i] = Pawn(-1)
        self.pos[0][7],self.pos[0][0] = Rook(1),Rook(1)
        self.pos[7][7],self.pos[7][0] = Rook(-1),Rook(-1)
        self.pos[0][6],self.pos[0][1] = Knight(1),Knight(1)
        self.pos[7][6],self.pos[7][1] = Knight(-1),Knight(-1)
        self.pos[0][5],self.pos[0][2] = Bishop(1),Bishop(1)
        self.pos[7][5],self.pos[7][2] = Bishop(-1),Bishop(-1)
        
        self.pos[0][3],self.pos[7][3] = Queen(1),Queen(-1)
        self.pos[0][4],self.pos[7][4] = King(1),King(-1)

    def print_board(self):
        for i in range(8):
            print(chr(97+i),end="   ")
        print("\n")
        for i in range(8):
            for j in range(8):
                ending ="   "
                if(self.pos[i][j].get_player()*self.pos[i][j].get_index()<0):
                    ending ="  "
                print(self.pos[i][j].get_player()*self.pos[i][j].get_index(),end=ending)
            print("   ",end="")
            print(i)
            print()

    def get_board_as_np_array(self):
        npboard = np.zeros((8,8))
        for i in range(8):
            for j in range(8):
                npboard[i][j]=self.pos[i][j].get_player()*self.pos[i][j].get_index()
        return npboard
    
    def is_legal_move(self,move,player):
        tempboard = copy.deepcopy(self)
        tempboard.make_move(move)
        if tempboard.check_for_check(player):   
            return False
        return True

    def get_all_moves(self,player):
        all_moves = []
        for i in range(8):
            for j in range(8):
                if self.pos[i][j].get_player() == player:
                    moves = self.pos[i][j].get_moves(self,i,j)
                    if moves is not None:
                        for entry in moves:
                            all_moves.append(entry)
        #print(all_moves)
        legal_moves=[]
        if all_moves is not None:
            for entry in all_moves:
                if self.is_legal_move(entry,player)==True:
                    legal_moves.append(entry)
        
        return legal_moves


    def get_all_non_king_moves(self,player):
        all_moves = []
        for i in range(8):
            for j in range(8):
                if self.pos[i][j].get_player() == player and self.pos[i][j].get_index()!=2:
                    moves = self.pos[i][j].get_moves(self,i,j)
                    if moves is not None:
                        for entry in moves:
                            all_moves.append(entry)
        return all_moves

    def make_move(self,move):
        if self.pos[move[1][0]][move[1][1]].get_index() == 0:
            self.turns_without_action = self.turns_without_action + 1
        else:
            self.turns_without_action = 0
        if len(move[1])==3:
            if move[1][2] == 3:
                self.pos[move[1][0]][move[1][1]] = Queen(self.pos[move[0][0]][move[0][1]].get_player())
                self.pos[move[0][0]][move[0][1]] = Empty()
                
            if move[1][2] == 4:
                self.pos[move[1][0]][move[1][1]] = Knight(self.pos[move[0][0]][move[0][1]].get_player())
                self.pos[move[0][0]][move[0][1]] = Empty()
                
            if move[1][2] == 5:
                self.pos[move[1][0]][move[1][1]] = Bishop(self.pos[move[0][0]][move[0][1]].get_player())
                self.pos[move[0][0]][move[0][1]] = Empty()
                
            if move[1][2] == 6:
                self.pos[move[1][0]][move[1][1]] = Rook(self.pos[move[0][0]][move[0][1]].get_player())
                self.pos[move[0][0]][move[0][1]] = Empty()
            return
        self.pos[move[1][0]][move[1][1]] = self.pos[move[0][0]][move[0][1]]
        self.pos[move[0][0]][move[0][1]] = Empty()
        if self.pos[move[1][0]][move[1][1]].get_index() in (1,2):
            self.pos[move[1][0]][move[1][1]].moved = True


    def find_king_position(self,player):
        for i in range(8):
            for j in range(8):
                if self.pos[i][j].get_player() == player and self.pos[i][j].get_index() == 2:
                    return (i,j)

    def check_for_check(self,player):
        #print("funktion wird aufgerufen")
        moves = self.get_all_non_king_moves(player*-1)
        tuples = self.find_king_position(player)
        
        for entry in moves:
            if tuples == entry[1][:2]:
                return True
        x2,y2 = self.find_king_position(-player)
        king_options = [(x2+1,y2+1),(x2+1,y2),(x2+1,y2-1),(x2,y2+1),(x2,y2-1),(x2-1,y2-1),(x2-1,y2),(x2-1,y2+1)]
        if tuples in king_options:
            return True 
        return False
    """    
    def check_for_checkmate(self,player):
        position = self.find_king_position(player)
        moves = self.pos[position[0]][position[1]].get_moves(self,position[0],position[1])
        if self.check_for_check(player)==True and moves == []:
            return True
        return False
    """

                


#print(neww.check_for_check(1))
#print(neww.get_all_moves(1))
#print(neww.check_for_checkmate(1))
#neww.make_move(((5,4),(6,4)))
#neww.print_board()










