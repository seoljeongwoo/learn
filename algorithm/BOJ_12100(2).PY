import sys
input =sys.stdin.readline
result = 0 
N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]
def rotate(Mp):
    global N
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = Mp[N-1-j][i]
    return temp

def DFS(M, dep):
    global result
    for data in M:
        result = max(result, max(data))
    if dep == 0:
        return
    for i in range(4):
        NewM = []
        for data in M:
            Q , NQ= [],[]
            for j in data:
                if j!= 0:
                    Q.append(j)
            for j in range(1,len(Q)):
                if Q[j-1] == Q[j]:
                    Q[j-1],Q[j] = Q[j-1]*2,0
            for j in Q:
                if j!= 0:
                    NQ.append(j)
            NewM.append(NQ + [0]*(N-len(NQ)))
        if NewM != M:
            DFS(NewM,dep-1)
        M = rotate(M)
    return
DFS(M,5)
print(result)