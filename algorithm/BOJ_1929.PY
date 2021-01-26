def e():
    c[1] = False
    for i in range(2,N+1):
        if i*i > N:
            break
        if c[i] == True:
            for j in range(i*i,N+1,i):
                c[j]=False
    return

M,N = map(int,input().split())
c = [True]*(N+1)
e()
for i in range(M,N+1):
    if c[i] == True:
        print(i)