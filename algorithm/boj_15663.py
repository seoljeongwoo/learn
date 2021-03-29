import sys
input = sys.stdin.readline

def back(st , pick):
    if len(pick) == m:
        if st in dic.keys(): return
        print(' '.join(map(str,pick)))
        dic[st] = True
        return
    for i in range(n):
        if v[i]: continue
        v[i] = True
        back(st + str(lst[i]) , pick + [lst[i]])
        v[i] = False
    return

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
dic = {}
v = [False] * n
back("",[])
