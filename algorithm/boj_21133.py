import sys
input = sys.stdin.readline

n = int(input().rstrip('\n'))
lst = []

if n%6==2:
    st = 2
    while st<=n: 
        lst.append(st)
        st+=2
    lst.append(3); lst.append(1)
    st = 7
    while st<=n: 
        lst.append(st)
        st+=2
    lst.append(5)
elif n%6==3:
    st=4
    while st<=n: 
        lst.append(st)
        st+=2
    lst.append(2)
    st=5
    while st<=n: 
        lst.append(st)
        st+=2
    lst.append(1); lst.append(3)
else:
    st = 2
    while st<=n: 
        lst.append(st)
        st+=2
    st = 1
    while st<=n: 
        lst.append(st)
        st+=2

for data in lst:
    print(data)