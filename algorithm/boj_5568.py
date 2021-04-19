import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
get = dict()
lst = [input().rstrip('\n') for _ in range(n)]
for data in list(permutations([i for i in range(n)] , k)):
    s = ""
    for index in data: s+= lst[index]
    if s not in get.keys(): get[s] = True
print(len(get))
    