import sys
from collections import Counter
N,M=map(int,input().split())
tree = Counter(map(int,input().split()))
lo,hi,result=0,max(tree)+1,1
while lo<=hi:
    mid = (lo+hi)//2
    _sum = 0
    for wood,cnt in tree.items():
        if wood>=mid:
            _sum += (wood-mid) * cnt
    if _sum >=M:
        result = mid
        lo = mid+1
    else:
        hi = mid-1
print(result)