import sys
input = sys.stdin.readline
N , T = int(input()), list(map(int,input().split()))
st , result = [], [0 for i in range(N)]
for i in range(0,N):
    while len(st) > 0 and T[st[-1]] <= T[i]:
        st.pop()
    if len(st) != 0 :
        result[i] = st[-1] + 1
    st.append(i)
print(*result)
         