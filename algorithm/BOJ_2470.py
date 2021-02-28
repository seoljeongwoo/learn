import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
lst.sort()
i,j=0,len(lst)-1
gap = 2000000001
p1,p2=0,0
while i<len(lst) and j>=0 and i<j:
    new_gap = abs(lst[i] + lst[j])
    
    if gap > new_gap:
        gap = new_gap
        p1,p2=min(lst[i],lst[j]),max(lst[i],lst[j])
    
    if lst[i] + lst[j] > 0:
        j -= 1
    elif lst[i] + lst[j] < 0:
        i += 1
    else: break 
print(p1,p2)