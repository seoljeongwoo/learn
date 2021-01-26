# def _back(p,pre):
#     if len(p) == M:
#         print(*p)
#         return
#     for i in range(pre,N+1):
#         p.append(i)
#         _back(p,i)
#         p.pop()
#     return
# N,M=map(int,input().split())
# _back([],1)

from itertools import combinations_with_replacement
N,M=map(int,input().split())
print('\n'.join(map(' '.join, combinations_with_replacement(map(str,range(1,N+1)),M))))