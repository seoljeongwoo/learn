import sys
input = sys.stdin.readline
N , lst = int(input()) , list(map(int,input().split()))
result , st = [ 0 for _ in range(N)] , []
for i in range(N-1 , -1, -1) :
    while len(st)>0 and st[-1]<= lst[i]:
            st.pop()
    if len(st) == 0: result[i] = -1
    else: result[i] = st[-1]
    st.append(lst[i])
print(*result)
