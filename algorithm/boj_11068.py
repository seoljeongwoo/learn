import sys
input = sys.stdin.readline

def digit(val , d):
    temp = []
    while val:
        temp.append(val%d)
        val//=d
    temp.reverse()
    return temp

def check(lst):
    size = len(lst)
    if size == 1: return True
    for i in range(size//2):
        if lst[i] != lst[size-1-i]:return False
    return True
    
t = int(input())
for _ in range(t):
    n = int(input())
    ok = False
    for i in range(2,65):
        new_lst = digit(n,i)
        if check(new_lst):
            ok = True
            break
    print(1 if ok else 0)