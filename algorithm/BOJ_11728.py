# import sys
# input = sys.stdin.readline
# A,B = map(int,input().split())
# lst = list(map(int,input().split())) + list(map(int, input().split()))
# print(' '.join(map(str,sorted(lst))))

import sys
input = sys.stdin.readline
input()
A,B = list(map(int,input().split())),list(map(int,input().split()))
R=[]
i,j=0,0
while i<len(A) and j<len(B):
    if A[i] < B[j]: 
        R.append(A[i])
        i+=1
    else:
        R.append(B[j])
        j+=1
while i<len(A):
    R.append(A[i])
    i+=1
while j<len(B):
    R.append(B[j])
    j+=1
print(' '.join(map(str,R)))