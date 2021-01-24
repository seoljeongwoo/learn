def rotate(state, lst):
    for i in range(4):
        if state[i] == 1:   # 시계
            v = lst[i].pop()
            lst[i] = [v] + lst[i]
        elif state[i] == -1: # 반시계
            v = lst[i].pop(0)
            lst[i].append(v)
    return

def go(state, curr, LR, clock):
     
    if LR == 1: # Right
        if curr + 1 >=4 :
            return
        if lst[curr][2] != lst[curr+1][6]:
            state[curr+1] = -1*clock
            go(state, curr+1, LR , -1*clock)
    else:   # Left
        if curr -1 <= -1:
            return
        if lst[curr][6] != lst[curr-1][2]:
            state[curr-1] = -1*clock
            go(state, curr-1, LR, -1*clock)
    return

lst = [list(input()) for _ in range(4)]
Query = int(input())

for _ in range(Query):
    N, clock = map(int,input().split())
    state = [0]*4
    state[N-1] = clock
    go(state , N-1, 1, clock)
    go(state , N-1, -1, clock)
    rotate(state,lst)

result = 0
for i in range(4):
    result += int(2**i) * i nt(lst[i][0])
print(result)
    