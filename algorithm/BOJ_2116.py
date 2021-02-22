import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def go(floor, value):
    if floor == N: return 0

    pick = 0
    for index , v in enumerate(lst[floor]):
        if value == v: 
            pick = index
            break
    
    ret = 6
    next_node = next_pick[pick]
    _Max = max(lst[floor][pick] , lst[floor][next_node])
    _Min = min(lst[floor][pick] , lst[floor][next_node])
    if ret == _Max : ret -=1
    if ret == _Min : ret -=1
    
    return ret + go(floor+1 , lst[floor][next_node])

N = int(input())
lst = []
next_pick = [5] + [3] + [4] + [1] + [2] + [0]
for _ in range(N):
    lst.append(list(map(int,input().split())))
result = 0
for _ in range(6):
    result = max(result , go(0,lst[0][_]))
print(result)