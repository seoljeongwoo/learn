import sys
input = sys.stdin.readline
ret = 0
for _ in range(int(input())):
    lst = input().split()
    op = lst[0]
    num = int(lst[1]) if op!= "all" and op!= "empty" else 0
    if op == "add":
        ret |= (1<<num)
    elif op == "remove":
        ret &= ~(1<<num)
    elif op == "check":
        if ret & (1<<num): print(1)
        else: print(0)
    elif op == "toggle":
        ret ^= (1<<num)
    elif op == "all":
        ret = (1<<21)-1
    elif op == "empty":
        ret = 0 