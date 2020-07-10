#import chessLogic as cl

def get_move_by_action(action):
    if action <= 4095 and action >= 0:
        move = ((int(action/512),int((action%512)/64)),(int(((action%512)%64)/8),((action%512)%64)%8))
    if action >= 4096 and action<= 4191:
        action = action - 4096
        move=((1,int(action/12)),(0,int(action/4)-2*int(action/12)-1,action%4+3))
    if action >= 4192 and action<= 4288:
        action = action - 4192
        move=((6,int(action/12)),(7,int(action/4)-2*int(action/12)-1,action%4+3))
    return move

for i in range(4095,4288):
    print(get_move_by_action(i))

def get_action_by_move(move):
    action = 10000
    if len(move[1])==2:
        action = move[0][0]*512+move[0][1]*64+move[1][0]*8+move[1][1]

    return action




move = ((0,0),(0,0))
action = get_action_by_move(move)
print(action)
move2 = get_move_by_action(action)
print(move2)

"""


valid = [0]*4096

for i in range(8):
    for j in range(8):
        for k in range(8):
            for l in range(8):
                move = ((i,j),(k,l))
                action = move[0][0]*512+move[0][1]*64+move[1][0]*8+move[1][1]
                valid[action] = valid[action]+1

print(valid)

move = ((2,2),(6,4))

action = move[0][0]*512+move[0][1]*64+move[1][0]*8+move[1][1]
print(action)

move2 = ((int(action/512),int((action%512)/64)),(int(((action%512)%64)/8),((action%512)%64)%8))
print(move2)


action = a*512+b*64+c*8+d
print(action)
a = int(action/512)
b = int((action%512)/64)
c = int(((action%512)%64)/8)
d = ((action%512)%64)%8
print(a)
print(b)
print(c)
print(d)

0 0 0 0     0
0 0 0 1     1
0 0 0 2     2
......
0 0 0 7     7
0 0 1 0     8

8^3*a+8^2*b+8^1*c+d = e
550 % 512 = 38
"""