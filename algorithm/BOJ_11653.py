N , p =int(input()), 2
if N==1:
    exit()
while p*p<=N:
    if N%p == 0:
        print(p)
        N//=p
    else:
        p+=1
if N>1:
    print(N)
