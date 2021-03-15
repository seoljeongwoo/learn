import sys
from collections import deque
input = sys.stdin.readline

def solve(start, end):
    v = [False]*10001
    q = deque()
    q.append((start, ""))
    v[start] = True
    while q:
        curr, op = q.popleft()
        if curr == end:
            print(op)
            return
        l,r = curr//1000, curr%10
        left ,right = (curr%1000)*10 + l , (curr//10) + r*1000 
        
        if not v[(2*curr)%10000] : 
            q.append(( (2*curr)%10000 , op + "D")); v[(2*curr)%10000] = True
        if not v[(curr+9999)%10000]:
            q.append(((curr+9999)%10000 , op +"S")); v[(curr+9999)%10000] = True
        if not v[right]:
            q.append((right, op +"R")); v[right] = True
        if not v[left]:
            q.append((left,op+"L")); v[left] = True
    return
        

tc = int(input())
for _ in range(tc):
    a,b=map(int,input().split())
    solve(a,b)