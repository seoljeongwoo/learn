import sys
from collections import deque
input = sys.stdin.readline
def bfs(st):
    des = "123456780"
    v = {}
    deq = deque()
    deq.append(des)
    v[des] = 0
    direction = [-3,-1,1,3]
    while deq:
        curr = deq.popleft()
        zero = curr.find('0')
        curr_lst = list(curr)
        for nx in direction :
            zero_nx = zero + nx
            if 0<= zero_nx <= 8 :
                if zero_nx//3 != zero//3 and zero_nx%3 != zero%3: continue
                curr_lst[zero+nx] , curr_lst[zero] = curr_lst[zero] , curr_lst[zero+nx]
                ne = ""
                for data in curr_lst: 
                    ne += data
                if ne not in v.keys():
                    v[ne] = v[curr] + 1
                    deq.append(ne)
                curr_lst[zero+nx] , curr_lst[zero] = curr_lst[zero] , curr_lst[zero+nx]
    if st in v.keys(): return v[st]
    else: return -1

s = ""
for _ in range(3):
    row = input().rstrip('\n').split()
    for data in row:
        s += data
print(bfs(s))