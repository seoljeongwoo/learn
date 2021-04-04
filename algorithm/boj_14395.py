import sys
from collections import deque
input = sys.stdin.readline

s,t= map(int,input().split())
if s==t: print(0);exit(0)
v = {}
v[s] = ""
lst = deque()
lst.append(s)
while lst:
    curr = lst.popleft()

    if curr*curr <= int(1e9) and curr*curr not in v.keys():
        v[curr*curr] = v[curr] + '*'
        lst.append(curr*curr)
    if curr+curr <= int(1e9) and curr+curr not in v.keys():
        v[curr+curr] = v[curr] + '+'
        lst.append(curr+curr)
    if curr-curr >0 and curr-curr not in v.keys():
        v[curr-curr] = v[curr] + '-'
        lst.append(curr-curr)
    if curr!=0 and curr//curr >0 and curr//curr not in v.keys():
        v[curr//curr] = v[curr] + '/'
        lst.append(curr//curr)
    if t in v.keys():
        print(v[t]); exit(0)
print(-1)