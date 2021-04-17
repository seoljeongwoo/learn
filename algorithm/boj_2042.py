import sys
input = sys.stdin.readline

def init():
    for i in range(N):
        seg[bit//2 + i] = A[i]
    for i in range((bit//2)-1 ,0 ,-1):
        seg[i] = seg[i*2] + seg[i*2+1]
    return

def update(i,c):
    index = (bit//2) + i
    seg[index] = c
    while index > 0:
        index //= 2
        seg[index] = seg[index*2] + seg[index*2+1]
    return

def query(left, right):
    left += (bit//2)
    right += (bit//2)
    ret = 0
    while left <right:
        if left%2 == 1:
            ret += seg[left]
            left +=1
        if right%2 == 0:
            ret += seg[right]
            right -=1
        left//=2
        right//=2
    if left == right: ret += seg[left]
    return ret

N,M,K = map(int,input().split())
A = list(int(input()) for _ in range(N))
bit =1
while bit < N: bit*=2
bit*=2
seg = [0]*bit
init()
for i in range(M+K):
    q,u,v = map(int,input().split())
    if q == 1:
        update(u-1,v)
    else:
        print(query(u-1,v-1))