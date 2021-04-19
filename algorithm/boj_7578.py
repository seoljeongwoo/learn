import sys
input = sys.stdin.readline

def Sum(index):
    s = 0
    while index:
        s += fenwick[index]
        index -= (index & -index)
    return s

def update(index, value):
    
    while index <= n:
        fenwick[index] += value
        index += ( index & -index)
    return

n = int(input())
fenwick= [0]*(n+1)
a = list(map(int,input().split()))
ai = dict()
for i in range(1,n+1):
    ai[a[i-1]]=i
b = list(map(int,input().split()))
ans = 0
for i in range(n):
    value = ai[b[i]]
    ans += (Sum(n) - Sum(value-1))
    update(value,1)
print(ans)