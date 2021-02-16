import sys
input = sys.stdin.readline
dic = dict()
input()
lst = list(map(int,input().split()))
for x in lst:
    if x in dic.keys() : dic[x] += 1
    else : dic[x] = 1
input()
lst = list(map(int,input().split()))
for x in lst:
    if x in dic.keys():
        print(dic[x] , end =" ")
    else:
        print(0,end= " ")