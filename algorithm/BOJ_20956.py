from collections import defaultdict
import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())
dic = defaultdict()
lst = list(map(int,input().split()))
Sorted = []
for index, value in enumerate(lst):
    Sorted.append((-value,index))
Sorted.sort()
for value, index in Sorted:
    if value not in dic.keys():
        dic[value] = deque()
    dic[value].append(index)
ok= 0
for _ in range(M):
    value = Sorted[_][0]
    if ok == 0:
        print(dic[value].popleft() + 1)
    else:
        print(dic[value].pop() + 1)
    if -1*value % 7 == 0: ok = 1-ok
