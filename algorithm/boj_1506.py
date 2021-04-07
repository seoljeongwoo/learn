import sys
input = sys.stdin.readline

def dfs(c):
    v[c] = True
    for n in e[c]:
        if v[n]==True: continue
        dfs(n)
    st.append(c)
    return
def rev_dfs(c):
    v[c] = True
    ret = [c]
    for n in rev_e[c]:
        if v[n] == True : continue
        ret += rev_dfs(n)
    return ret
n = int(input())
cost = list(map(int,input().split()))
edge = [list(map(int,list(input().rstrip('\n')))) for _ in range(n)]
e = [ [] for _ in range(n+1)]
rev_e = [ [] for _ in range(n+1)]
for i,row in enumerate(edge):
    for j,col in enumerate(row):
        if col == 1: e[i].append(j); rev_e[j].append(i)
v = [False] * n
st = []
for i in range(n):
    if v[i] == False: dfs(i)
v = [False] * n
ret = 0
while st:
    t = st.pop()
    if v[t] == True: continue
    scc_lst = rev_dfs(t)
    min_cost = int(1e6)
    for data in scc_lst:
        min_cost = min(min_cost, cost[data])
    ret += min_cost
print(ret)
 