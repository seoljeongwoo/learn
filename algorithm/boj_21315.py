import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def mix(a, k):
    if k==-1: return a
    po = 2**k
    index = len(a) - po
    return mix(a[index:],k-1) + a[:index]

def check(a, b):
    for i in range(len(a)):
        if a[i] != b[i]: return False
    return True

n = int(input())
target = list(map(int,input().split()))

for i in range(1,n):    #first k
    if 2**i >= n: break
    lst = [i+1 for i in range(n)]
    lst = mix(lst,i)
    for j in range(1,n):    # second k
        if 2**j >= n: break
        temp = deepcopy(lst)
        temp = mix(temp,j)
        if check(temp, target):
            print(i,j)
            exit(0)
        