import sys
input = sys.stdin.readline
N = int(input())
lst = [ i for i in range(1,N+1)]
while len(lst)>1:
    if len(lst)%2 == 0: lst = lst[1::2]
    else: lst = [lst[-1]] + lst[1:-1:2]
print(lst[0])