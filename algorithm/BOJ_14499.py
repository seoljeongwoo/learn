import sys
input = sys.stdin.readline
N,M,X,Y,K=map(int,input().rstrip('\n').split())
Map = []
for _ in range(N):
    Map.append(list(map(int,input().rstrip('\n').split())))
OP = list(map(int,input().rstrip('\n').split()))
Board = [0]*6   # up , down, left, right, front, back
direction = [(0,1), (0,-1) , (-1,0), (1,0)]
for op in OP:
    op -= 1
    nx ,ny = X+direction[op][0] , Y+direction[op][1]
    if nx == -1 or nx == N or ny == -1 or ny == M: continue
    if op == 0:     # E
        Board[0],Board[1],Board[2],Board[3] = Board[2],Board[3],Board[1],Board[0]
    elif op == 1:   # W
        Board[0],Board[1],Board[2],Board[3] = Board[3],Board[2],Board[0],Board[1]
    elif op ==2:    # N
        Board[0],Board[1],Board[4],Board[5] = Board[4],Board[5],Board[1],Board[0]
    else:           # S
        Board[0],Board[1],Board[4],Board[5] = Board[5],Board[4],Board[0],Board[1]
    if Map[nx][ny] == 0 :
        Map[nx][ny] =Board[1]
    else:
        Board[1],Map[nx][ny] = Map[nx][ny] , 0
    print(Board[0])
    X,Y= nx,ny

