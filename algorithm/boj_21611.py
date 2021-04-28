import sys
input = sys.stdin.readline

one,two,three =0,0,0
def make_order():
    ret = []
    direction = [(0,-1), (1,0), (0,1), (-1,0)]
    x,y,d= n//2,n//2,0
    cnt,mn,mncnt=0,1,0
    while True:
        nx,ny = x + direction[d][0], y+direction[d][1]
        ret.append((nx,ny))
        cnt+=1
        if cnt == mn:
            cnt = 0
            mncnt += 1
            d = (d+1)%4
        if mncnt == 2:
            mn+=1
            mncnt = 0
        if nx == 0 and ny == 0: break
        x,y = nx,ny
    return ret

def move():
    i,j=0,0
    temp = [ [0]*n for _ in range(n)]
    while i<len(orders) and j<len(orders):
        while j<len(orders):
            if board[orders[j][0]][orders[j][1]] != 0: break
            j+=1
        if j<len(orders) : temp[orders[i][0]][orders[i][1]] = board[orders[j][0]][orders[j][1]]
        i+=1; j+=1
    
    return temp

def bomb():
    global one, two, three
    erase = []
    cnt = 1
    for i in range(1,len(orders)):
        if board[orders[i-1][0]][orders[i-1][1]] == board[orders[i][0]][orders[i][1]]: cnt+=1
        else:
            if board[orders[i-1][0]][orders[i-1][1]] != 0 and cnt >= 4: erase.append((i-1,cnt))
            cnt = 1
    if board[orders[-1][0]][orders[-1][1]] !=0 and cnt >=4: erase.append((len(orders)-1,cnt))
    if len(erase) == 0: return False

    for data in erase:
        if board[orders[data[0]][0]][orders[data[0]][1]] == 1: one+= data[1]
        elif board[orders[data[0]][0]][orders[data[0]][1]] == 2: two+= 2*data[1]
        elif board[orders[data[0]][0]][orders[data[0]][1]] == 3: three += 3*data[1]
        for j in range(data[0],data[0]-data[1],-1):
            board[orders[j][0]][orders[j][1]] = 0
    return True

def group():

    process = 0
    cnt = 1
    temp = [[0]*n for _ in range(n)]
    for i in range(1,len(orders)):
        if process >= len(orders): break
        if board[orders[i-1][0]][orders[i-1][1]] == board[orders[i][0]][orders[i][1]]: cnt +=1
        else:
            a,b = cnt, board[orders[i-1][0]][orders[i-1][1]]
            if b != 0:
                temp[orders[process][0]][orders[process][1]] = a
                temp[orders[process+1][0]][orders[process+1][1]] = b
                process += 2
            cnt = 1
    if board[orders[-1][0]][orders[-1][1]] !=0:
        a,b = cnt, board[orders[-1][0]][orders[-1][1]]
        temp[orders[process][0]][orders[process][1]] = a
        temp[orders[process+1][0]][orders[process+1][1]] = b
    return temp

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
orders = make_order()
direction = [(-1,0) , (1,0), (0,-1), (0,1)]

for _ in range(m):
    sx,sy = n//2,n//2
    d, s = map(int,input().split())
    d-=1

    for i in range(1,s+1):
        nx,ny = sx + direction[d][0] * i , sy + direction[d][1] * i
        if 0<=nx<n and 0<=ny<n:
            board[nx][ny] = 0

    while True:
        board = move()
        if not bomb(): break

    board = group()
print(one+two+three)