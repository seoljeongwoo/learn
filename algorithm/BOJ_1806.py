import sys
input = sys.stdin.readline
n,s = map(int,input().split())
lst = list(map(int,input().split()))
i,j=0,0
presum = 0
result = 100001
while j < n:
    if presum < s:
        presum += lst[j]
        j+=1
    else:
        result = min(result , j-i)
        presum -= lst[i]
        i+=1
while i < n:
    if presum < s: break
    result = min(result, j-i)
    presum -= lst[i]
    i+=1
if result == 100001: result = 0
print(result)