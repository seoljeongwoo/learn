from collections import deque
import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    p,n,x = input().rstrip('\n'), int(input()), deque(input().lstrip('[').rstrip(']\n').split(','))
    r,e=0,0
    for o in p:
        if o == 'R': r += 1
        else:
            if n > 0 and r%2 ==1: x.pop();n-=1
            elif n>0 and r%2 ==0: x.popleft();n-=1
            else: e=1;break
    x = list(x)
    if r%2 == 1: x.reverse()
    if e: print("error")
    else: print("[",end="");print(','.join(map(str,x)),end="");print("]")
