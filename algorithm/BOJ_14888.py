m,n=-1000000001,1000000001
def cal(p):
    global m,n
    v = A[0]
    for i in range(len(p)):
        if p[i] == 0: v += A[i+1]
        elif p[i]==1: v -= A[i+1]
        elif p[i]==2: v *= A[i+1]
        else: 
            if v < 0 : 
                v *= -1
                v//=A[i+1]
                v *= -1
            else: v//=A[i+1]
    m = max(m,v)
    n = min(n,v)
    return

def back(p, op):
    if max(op) == 0:
        cal(p)
        return
    for i in range(4):
        if op[i] == 0: continue
        p.append(i)
        op[i] -= 1
        back(p,op)
        op[i] += 1
        p.pop()
    return

N = int(input())
A = list(map(int ,input().split()))
op = list(map(int,input().split()))
back([],op)
print(m)
print(n)