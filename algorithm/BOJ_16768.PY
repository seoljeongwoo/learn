from collections import deque
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
_input = []
for _ in range(N):
    _input.append(input())
pooyo = []
for i in range(len(_input)):
    pooyo.append([])
    for j in _input[i]:
        pooyo[i].append(j)
dx,dy = [-1,0,1,0] , [0,1,0,-1]

def bfs(x,y,visited,group):
    queue = deque()
    queue.append((x,y))
    color ,count = pooyo[x][y], 0
    while queue:
        cx,cy = queue.popleft()
        if visited[cx][cy] != 0: continue
        visited[cx][cy] = group
        count += 1

        for i in range(4):
            nx,ny = cx+dx[i], cy + dy[i]
            if nx<0 or nx==N or ny <0 or ny==10: continue
            if visited[nx][ny] != 0: continue
            if pooyo[nx][ny] != color: continue
            queue.append((nx,ny))
    if count < K:
        return False
    else:
        global ok
        ok = True
        for i in range(N):
            for j in range(10):
                if visited[i][j] == group:
                    pooyo[i][j] = '0'
        return True

while True:
    
    ok = False
    # K칸 이상인 color 삭제
    visited = [[0]*10 for _ in range(N)]
    group = 1
    for i in range(N):
        for j in range(10):
            if pooyo[i][j] == '0': continue
            if visited[i][j] != 0 : continue
            ok |= bfs(i,j,visited,group)
            group += 1
    # gravity 구현
    for i in range(N-1,-1,-1):
        for j in range(10):
            if pooyo[i][j] == '0': continue
            cx,cy = i, j
            while cx+1<N and pooyo[cx+1][cy] == '0':
                cx += 1
            if cx != i :
                pooyo[cx][cy] , pooyo[i][j] = pooyo[i][j] , '0'
    
    if ok == False:
        break
for data in pooyo:
    print(''.join(map(str,data)) , end = "")
