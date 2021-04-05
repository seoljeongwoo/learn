import sys
input = sys.stdin.readline

n,k = map(int,input().split())
lst = list(map(int,input().split()))
i,j,dic=0,0,{}
ret = 0
for data in lst: dic[data] =0
while i<n and j<n:
    ret = max(ret,i-j)
    if dic[lst[i]] < k:
        dic[lst[i]] += 1
        i+=1
    else:
        dic[lst[j]] -= 1
        j+=1
ret = max(ret,i-j)
print(ret)