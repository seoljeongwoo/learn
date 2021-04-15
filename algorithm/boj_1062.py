import sys
from itertools import combinations
input = sys.stdin.readline

n,k = map(int,input().split())
if k < 5: print(0); exit(0)
k-=5
base = set("acnit")
convert = {chr(i+ord('a')) : 1<<i for i in range(26)}
temp = []
learn = set()
ans = 0
for data in list(input().rstrip('\n') for _ in range(n)):
    data = set(data) - base
    if len(data) == 0: 
        ans += 1
        continue
    learn |= data
    bit = 0
    for alpha in data: bit += convert[alpha]
    temp.append(bit)
new_learn = []
for x in learn: new_learn.append(convert[x])
ret = 0
for data in list(combinations(new_learn , min(k, len(new_learn)))):
    s = sum(data)
    cnt = 0 
    for bit in temp:
        if s & bit == bit: cnt +=1
    ret = max(ret,cnt)
print(ret + ans)

