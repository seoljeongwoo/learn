import sys
input = sys.stdin.readline

N = int(input())
prime = [True] * (N+1)
for i in range(2,int(N**0.5)+1):
    if prime[i] == False: continue
    for j in range(i*i,N+1,i): prime[j] = False
p = []
for i in range(2,N+1):
    if prime[i]: p.append(i)
i,j = 0,0
size, s = len(p),0
ans = 0
while j<size:
    if s == N: ans +=1
    if s <= N: 
        s += p[j]
        j+=1
    else:
        s -= p[i]
        i+=1
while i<size :
    if s == N: ans +=1
    s -= p[i]
    i+=1
print(ans)