# def backtracking(pick):
#     if len(pick) == M:
#         print(*pick)
#         return
#     for i in range(1,N+1):
#         pick.append(i)
#         backtracking(pick)
#         pick.pop()
#     return
# N,M = map(int,input().split())
# backtracking([])

import itertools
N,M= map(int,input().split())
print("\n".join(map(' '.join, itertools.product(map(str,range(1,N+1)),repeat=M))))