def e():
    c[1] = False
    for i in range(2,int((N)**0.5) +1):
        if c[i] == True:
            for j in range(i*i,N+1,i):
                c[j] = False
    return
N = 123456*2
c = [True] * (N+1)
e()
while True:
    M = int(input())
    if M ==0:
        break
    else:
        print(c[M+1:2*M+1].count(True))