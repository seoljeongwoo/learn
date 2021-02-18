N = int(input())
if N==1:
    print('*')
    exit(0)

for i in range(2*N):
    if i%2 == 0:
        for j in range(N):
            if j%2 == 0: print('*',end="")
            else : print(' ',end="")
    else:
        for j in range(N):
            if j%2 == 0: print(' ',end="")
            else: print('*',end="")
    print()