import sys
input = sys.stdin.readline

def getpi(pi,size,P):

    j = 0
    for i in range(1,size):
        while j>0 and P[i] != P[j]: j = pi[j-1]
        if P[i] == P[j]:
            j+=1
            pi[i] = j
    return pi

def kmp(S,P):
    pi = [0] * len(P)
    pi = getpi(pi,len(P),P)

    j = 0
    size = len(S)
    for i in range(size):
        while j>0 and S[i] != P[j]: j = pi[j-1]

        if S[i] == P[j]:
            if j == len(P)-1: return True
            else : j+=1
    return


S = input().rstrip('\n')
P = input().rstrip('\n')
size = len(S)

if kmp(S,P): print(1)
else: print(0)