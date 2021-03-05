import sys
from collections import deque
input = sys.stdin.readline
n,w,l = map(int,input().split())
truck = list(map(int,input().split()))
q = deque()
t = [0]*(n+1)
t[0] = 1
truck_sum = truck[0]
front_truck = 0 
for i in range(1,n):
    while truck_sum + truck[i] > l or i-front_truck == w:
        truck_sum -= truck[front_truck]
        front_truck +=1
    truck_sum += truck[i]
    if front_truck==0:
        t[i] = t[i-1] + 1
    else:
        t[i] = max(t[i-1]+1, t[front_truck-1]+w)
print(t[n-1]+w)
