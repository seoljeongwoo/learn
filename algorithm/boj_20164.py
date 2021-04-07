import sys
input = sys.stdin.readline

def solve(v):
    if len(v) ==0: return int(1e9), -int(1e9)
    int_v= int(v)
    if int_v<=9: return int_v%2,int_v%2
    if int_v<=99:
        ret = 0
        for data in v: ret += 1 if int(data)%2 == 1 else 0
        new_v = int(v[0]) + int(v[1])
        a,b = solve(str(new_v))
        return ret+a, ret+b
    ret = 0
    min_v = int(1e9)
    max_v = -int(1e9)
    for data in v: ret += 1 if int(data)%2 == 1 else 0
    for i in range(1,len(v)):
        for j in range(i+1,len(v)):
            left,mid,right = int(v[:i]), int(v[i:j]), int(v[j:])
            new_v = str(left+mid+right)
            a,b = solve(str(new_v))
            min_v = min(min_v,a)
            max_v = max(max_v,b)
    return ret + min_v, ret+ max_v

        
n = input().rstrip('\n')
a,b= solve(n)
print(a,b)