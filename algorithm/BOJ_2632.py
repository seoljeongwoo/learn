import sys
input = sys.stdin.readline

size = int(input())
a,b=map(int,input().split())
pa = [int(input()) for _ in range(a)]
pb = [int(input()) for _ in range(b)]
sa,sb=[],[]
sa+=pa;sb+=pb
sa.append(sum(pa))
sb.append(sum(pb))
pa+=pa; pb+=pb
for k in range(2,a):
    s = sum(pa[0:k])
    j=k 
    for i in range(a):
        sa.append(s)
        s-=pa[i]
        s+=pa[j]
        j+=1
for k in range(2,b):
    s = sum(pb[0:k])
    j=k
    for i in range(b):
        sb.append(s)
        s-=pb[i]
        s+=pb[j]
        j+=1
sa.sort(); sb.sort()
ret = sa.count(size) + sb.count(size)
i,j=0,len(sb)-1
while i<len(sa) and j>=0:
    s = sa[i] + sb[j]
    if s > size:
        j-=1
    elif s<size:
        i+=1
    else:
        ni,nj=i+1,j-1
        while ni<len(sa) and sa[i]==sa[ni]:ni+=1
        while nj>=0 and sb[j] == sb[nj]:nj-=1
        ret += (ni-i)*(j-nj)
        i,j=ni,nj
print(ret)