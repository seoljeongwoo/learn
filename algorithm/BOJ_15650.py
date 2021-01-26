from itertools import combinations
N,M=map(int,input().split())
lst = [i for i in range(1,N+1)]
lst = list(combinations(lst,M))
for x in lst:
    print(*x)