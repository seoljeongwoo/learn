import sys
input = sys.stdin.readline

def dfs(curr):
    v[curr] =True
    for nx,nw in edge[curr]:
        if v[nx]: continue
        houseSp_table[nx][0] = curr
        moneySp_table[nx][0] = nw
        dfs(nx)
    return

max_d = 18
n = int(input())
lst = [0] + [int(input()) for _ in range(n)]
edge = [ [] for _ in range(n+1)]
for  _ in range(n-1):
    a,b,c = map(int,input().split())
    edge[a].append((b,c))
    edge[b].append((a,c))

houseSp_table = [[0]*max_d for _ in range(n+1)]
moneySp_table = [[0]*max_d for _ in range(n+1)]
v = [False] * (n+1)
dfs(1)

for j in range(1,max_d):
    for i in range(1,n+1):
        houseSp_table[i][j] = houseSp_table[houseSp_table[i][j-1]][j-1]
        moneySp_table[i][j] = moneySp_table[i][j-1] + moneySp_table[houseSp_table[i][j-1]][j-1]
ret = []
for i in range(1,n+1):
    get_money = lst[i]
    x = i
    for bit in range(max_d-1,-1,-1):
        if get_money >= moneySp_table[x][bit]:
            get_money -= moneySp_table[x][bit]
            x = houseSp_table[x][bit]
    if x ==0: x=1
    ret.append(x)
print(*ret) 