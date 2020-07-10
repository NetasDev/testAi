import numpy as np
import sys
from termcolor import cprint
import copy

class board():
    def __init__(self):
        self.has_already_moved = False
        self.turns_without_action = 0
        self.pawn_direction = 1
        self.has_not_moved = [(0,0),(0,7),(7,0),(7,7),(0,4),(7,4)]
        self.pieces = np.zeros((8,8),dtype=int)
        #Representation of Chess piecess as Numbers:
        #Pawn = 1;King = 2;Queen = 3;Knight = 4;Bishop = 5;Rook = 6; Leer = 0
        for i in range(8):
            self.pieces[1][i] = 1
            self.has_not_moved.append((1,i))
            self.has_not_moved.append((6,i))
        self.pieces[0][7],self.pieces[0][0] = 6,6
        self.pieces[0][5],self.pieces[0][2] = 5,5
        self.pieces[0][6],self.pieces[0][1] = 4,4
        self.pieces[0][3] = 3
        self.pieces[0][4] = 2
        for i in range(8):
            for j in range(2):
                self.pieces[7-j][i] = -1 * self.pieces[j][i]
    
    def print_board(self):
        for i in range(8):
            #print(chr(97+i),end="   ")
            print(i,end="   ")
        print("\n")
        print()
        for i in range(8):
            for j in range(8):
                
                if self.pieces[i][j]<0:
                    if(abs(self.pieces[i][j])==1):
                        cprint("P","cyan",end="   ")
                    if(abs(self.pieces[i][j])==2):
                        cprint("K","cyan",end="   ")
                    if(abs(self.pieces[i][j])==3):
                        cprint("Q","cyan",end="   ")
                    if(abs(self.pieces[i][j])==4):
                        cprint("N","cyan",end="   ")
                    if(abs(self.pieces[i][j])==5):
                        cprint("B","cyan",end="   ")
                    if(abs(self.pieces[i][j])==6):
                        cprint("R","cyan",end="   ")
                if self.pieces[i][j]==0:
                    cprint("0","grey",end="   ")
                if self.pieces[i][j]>0:
                    if(abs(self.pieces[i][j])==1):
                        print("P",end="   ")
                    if(abs(self.pieces[i][j])==2):
                        print("K",end="   ")
                    if(abs(self.pieces[i][j])==3):
                        print("Q",end="   ")
                    if(abs(self.pieces[i][j])==4):
                        print("N",end="   ")
                    if(abs(self.pieces[i][j])==5):
                        print("B",end="   ")
                    if(abs(self.pieces[i][j])==6):
                        print("R",end="   ")
            print("   ",end="")
            print(i)
            print()
    def get_all_moves(self,player):
        all_moves = []
        for i in range(8):
            for j in range(8):
                if player*self.pieces[i][j]>0:
                    moves = self.get_moves(i,j)
                    if moves is not None:
                        for entry in moves:
                            all_moves.append(entry)
        legal_moves = []
        if all_moves is not None:
            for entry in all_moves:
                if self.is_legal_move(entry,player):
                    legal_moves.append(entry)
        return legal_moves

    def get_moves(self,x,y):
        moves = []
        owner = int(abs(self.pieces[x][y])/self.pieces[x][y])
        if abs(self.pieces[x][y])==1:
            player = int(abs(self.pieces[x][y])/self.pieces[x][y])
            if self.is_in_bound(x+self.pawn_direction*player,y):
                if self.pieces[x+self.pawn_direction*player][y]==0:
                    if x+self.pawn_direction*player!=7 and x+self.pawn_direction*player!=0:
                        moves.append(((x,y),(x+self.pawn_direction*player,y)))
                    else:
                        for i in (3,4,5,6):
                            moves.append(((x,y),(x+self.pawn_direction*player,y,i)))
            if self.is_in_bound(x+2*self.pawn_direction*player,y):
                if (x,y) in self.has_not_moved:
                    if self.pieces[x+self.pawn_direction*player][y]==0 and self.pieces[x+2*self.pawn_direction*player][y]==0:
                        moves.append(((x,y),(x+2*self.pawn_direction*player,y)))

            #nach rechts schlagen
            if self.is_in_bound(x+self.pawn_direction*player,y+1):
                if self.pieces[x+self.pawn_direction*player][y+1]*self.pieces[x][y]<0:
                    if x+self.pawn_direction*player!=7 and x+self.pawn_direction*player!= 0:
                        moves.append(((x,y),(x+self.pawn_direction*player,y+1)))
                    else:
                        for i in (3,4,5,6):
                            moves.append(((x,y),(x+self.pawn_direction*player,y+1,i)))
            #nach links schlagen
            if self.is_in_bound(x+self.pawn_direction*player,y-1):
                if self.pieces[x+self.pawn_direction*player][y-1]*self.pieces[x][y]<0:
                    if x+self.pawn_direction*player!=7 and x+self.pawn_direction*player!= 0:
                        moves.append(((x,y),(x+self.pawn_direction*player,y-1)))
                    else:
                        for i in (3,4,5,6):
                            moves.append(((x,y),(x+self.pawn_direction*player,y-1,i)))

        if abs(self.pieces[x][y])==2:
            options = [(x+1,y+1),(x+1,y),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1)]
            for entry in options:
                if self.is_in_bound(entry[0],entry[1]):
                    if owner*self.pieces[entry[0]][entry[1]]<=0:
                        moves.append(((x,y),(entry[0],entry[1])))
        if abs(self.pieces[x][y])==3:
            motions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
            moves = self.repeat_motion(self,motions,x,y)
        if abs(self.pieces[x][y])==4:
            options = [(x+2,y+1),(x+2,y-1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2),(x-2,y+1),(x-2,y-1)]
            for entry in options:
                if self.is_in_bound(entry[0],entry[1]):
                    if self.pieces[x][y]*self.pieces[entry[0]][entry[1]]<=0:
                        moves.append(((x,y),(entry[0],entry[1])))
        
        if abs(self.pieces[x][y])==5:
            motions = [(1,1),(1,-1),(-1,1),(-1,-1)]
            moves = self.repeat_motion(self,motions,x,y)
        if abs(self.pieces[x][y])==6:
            motions = [(1,0),(0,1),(-1,0),(0,-1)]
            moves = self.repeat_motion(self,motions,x,y)
        
        
        return moves

    def make_move(self,move):
        if self.pieces[move[1][0]][move[1][1]]== 0:
            self.turns_without_action = self.turns_without_action + 1
        else:
            self.turns_without_action = 0
        if len(move[1])==3:
            self.pieces[move[1][0]][move[1][1]] = move[1][2]*self.pieces[move[0][0]][move[0][1]]/int(abs(self.pieces[move[0][0]][move[0][1]]))
            self.pieces[move[0][0]][move[0][1]] = 0
        
        self.pieces[move[1][0]][move[1][1]] = self.pieces[move[0][0]][move[0][1]]
        self.pieces[move[0][0]][move[0][1]] = 0
        if (move[0],move[1]) in self.has_not_moved:
            self.has_not_moved.remove((move[0],move[1]))
            print("piece now moved")
        self.has_already_moved = True

    def check_for_check(self,player):
        moves = self.get_all_non_king_moves(player*-1)
        
        king_position = self.find_king_position(player)
        for entry in moves:
            if king_position == entry[1][:2]:
                return True
        x2,y2 = self.find_king_position(-player)
        enemy_king_options = [(x2+1,y2+1),(x2+1,y2),(x2+1,y2-1),(x2,y2+1),(x2,y2-1),(x2-1,y2-1),(x2-1,y2),(x2-1,y2+1)]
        if king_position in enemy_king_options:  
            return True 
        return False

    def get_all_non_king_moves(self,player):
        all_moves = []
        for i in range(8):
            for j in range(8):
                if abs(self.pieces[i][j])!=2:
                    if player*self.pieces[i][j]>0:
                        moves = self.get_moves(i,j)
                        if moves is not None:
                            for entry in moves:
                                all_moves.append(entry)
        return all_moves

    def is_legal_move(self,move,player):
        tempboard = copy.deepcopy(self)
        tempboard.make_move(move)
        if tempboard.check_for_check(player):   
            return False
        return True

    def find_king_position(self,player):
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j] == player*2:
                    return (i,j)

    
    def is_in_bound(self,x,y):
        if x<=7 and y<=7 and x>=0 and y>=0:
            return True
        return False

    def repeat_motion(self,board,motions,x,y):
        owner = int(abs(self.pieces[x][y])/self.pieces[x][y])
        moves = []
        for addx,addy in motions:
            xnew,ynew = x+addx,y+addy
            while self.is_in_bound(xnew,ynew):
                field = board.pieces[xnew][ynew]
                if field == 0:
                    moves.append(((x,y),(xnew,ynew)))
                    
                elif field*owner<0:
                    moves.append(((x,y),(xnew,ynew)))
                    break
                else:
                    break
                xnew,ynew = xnew+addx,ynew+addy
        return moves
    
    def check_for_game_end(self,player):
        if self.turns_without_action >= 40:
            return 0.01
        if self.has_already_moved == False:
            if self.get_all_moves(player) == []:
                if self.check_for_check(player)==True:
                    return player*-1
                return 0.01
        else:
            if self.get_all_moves(-player)==[]:
                if self.check_for_check(-player)==True:
                    return player
                return 0.01
        return 0

    
    
neww = board()
player = 1
while(True):
    print(neww.check_for_game_end(player))
    neww.print_board()
    moves = neww.get_all_moves(player)
    while(True):
        print(moves)
        a = input()
        b = input()
        c = input()
        d = input()
        move = ((int(a),int(b)),(int(c),int(d)))
        print(move)
        if move in moves:
            break
    neww.make_move(move)
    player = player*-1
    neww.has_already_moved = False
    



print(neww.pieces)
print(neww.has_not_moved)
neww.print_board()
print(neww.get_all_moves(-1))





"""
class Board():
    
    def get_all_moves(self,player):
        all_moves = []
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j].get_player() == player:
                    moves = self.pieces[i][j].get_moves(self,i,j)
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

    def make_move(self,move):
        if self.pieces[move[1][0]][move[1][1]].get_index() == 0:
            self.turns_without_action = self.turns_without_action + 1
        else:
            self.turns_without_action = 0
        if len(move[1])==3:
            if move[1][2] == 3:
                self.pieces[move[1][0]][move[1][1]] = Queen(self.pieces[move[0][0]][move[0][1]].get_player())
                self.pieces[move[0][0]][move[0][1]] = Empty()
                
            if move[1][2] == 4:
                self.pieces[move[1][0]][move[1][1]] = Knight(self.pieces[move[0][0]][move[0][1]].get_player())
                self.pieces[move[0][0]][move[0][1]] = Empty()
                
            if move[1][2] == 5:
                self.pieces[move[1][0]][move[1][1]] = Bishop(self.pieces[move[0][0]][move[0][1]].get_player())
                self.pieces[move[0][0]][move[0][1]] = Empty()
                
            if move[1][2] == 6:
                self.pieces[move[1][0]][move[1][1]] = Rook(self.pieces[move[0][0]][move[0][1]].get_player())
                self.pieces[move[0][0]][move[0][1]] = Empty()
            return
        self.pieces[move[1][0]][move[1][1]] = self.pieces[move[0][0]][move[0][1]]
        self.pieces[move[0][0]][move[0][1]] = Empty()
        if self.pieces[move[1][0]][move[1][1]].get_index() in (1,2):
            self.pieces[move[1][0]][move[1][1]].moved = True

    def is_legal_move(self,move,player):
        tempboard = copy.deepcopy(self)
        tempboard.make_move(move)
        if tempboard.check_for_check(player):   
            return False
        return True

    


    def get_all_non_king_moves(self,player):
        all_moves = []
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j].get_player() == player and self.pieces[i][j].get_index()!=2:
                    moves = self.pieces[i][j].get_moves(self,i,j)
                    if moves is not None:
                        for entry in moves:
                            all_moves.append(entry)
        return all_moves

    def make_move(self,move):
        if self.pieces[move[1][0]][move[1][1]].get_index() == 0:
            self.turns_without_action = self.turns_without_action + 1
        else:
            self.turns_without_action = 0
        if len(move[1])==3:
            if move[1][2] == 3:
                self.pieces[move[1][0]][move[1][1]] = Queen(self.pieces[move[0][0]][move[0][1]].get_player())
                self.pieces[move[0][0]][move[0][1]] = Empty()
                
            if move[1][2] == 4:
                self.pieces[move[1][0]][move[1][1]] = Knight(self.pieces[move[0][0]][move[0][1]].get_player())
                self.pieces[move[0][0]][move[0][1]] = Empty()
                
            if move[1][2] == 5:
                self.pieces[move[1][0]][move[1][1]] = Bishop(self.pieces[move[0][0]][move[0][1]].get_player())
                self.pieces[move[0][0]][move[0][1]] = Empty()
                
            if move[1][2] == 6:
                self.pieces[move[1][0]][move[1][1]] = Rook(self.pieces[move[0][0]][move[0][1]].get_player())
                self.pieces[move[0][0]][move[0][1]] = Empty()
            return
        self.pieces[move[1][0]][move[1][1]] = self.pieces[move[0][0]][move[0][1]]
        self.pieces[move[0][0]][move[0][1]] = Empty()
        if self.pieces[move[1][0]][move[1][1]].get_index() in (1,2):
            self.pieces[move[1][0]][move[1][1]].moved = True


    def find_king_piecesition(self,player):
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j].get_player() == player and self.pieces[i][j].get_index() == 2:
                    return (i,j)

    def check_for_check(self,player):
        #print("funktion wird aufgerufen")
        moves = self.get_all_non_king_moves(player*-1)
        tuples = self.find_king_piecesition(player)
        
        for entry in moves:
            if tuples == entry[1][:2]:
                return True
        x2,y2 = self.find_king_piecesition(-player)
        king_options = [(x2+1,y2+1),(x2+1,y2),(x2+1,y2-1),(x2,y2+1),(x2,y2-1),(x2-1,y2-1),(x2-1,y2),(x2-1,y2+1)]
        if tuples in king_options:
            return True 
        return False
"""