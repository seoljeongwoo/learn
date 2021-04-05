import sys
from collections import deque
input = sys.stdin.readline

do,su = deque() , deque()
n,m = map(int,input().split())
for _ in range(n):
    u,v = map(int,input().split())
    do.appendleft(u)
    su.appendleft(v)
ground_do = deque()
ground_su = deque()
turn = 0
for _ in range(m):

    if _%2 == 0: ground_do.appendleft(do.popleft())
    else: ground_su.appendleft(su.popleft())

    if len(do) ==0 or len(su) ==0 : break

    if (len(ground_do) > 0 and ground_do[0] == 5) or (len(ground_su) >0 and ground_su[0] ==5):
        # winner do
        while ground_su:
            do.append(ground_su.pop())
        while ground_do:
            do.append(ground_do.pop())
    
    if len(ground_do) >0 and len(ground_su) > 0 and ground_do[0] + ground_su[0] == 5:
        # winner su
        while ground_do:
            su.append(ground_do.pop())
        while ground_su:
            su.append(ground_su.pop())


if len(do) < len(su): print("su")
elif len(do) > len(su): print("do")
else :print("dosu")
