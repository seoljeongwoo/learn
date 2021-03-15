import sys
input = sys.stdin.readline
n = int(input())
weight = list(map(int,input().split()))
dic = dict()
dic[weight[0]] = True
for _ in range(1,n):
    new_dic = dict()
    for x in dic.keys():
        new_dic[abs(weight[_] - x)] = True
        new_dic[weight[_] + x] = True
        new_dic[x]= True
    new_dic[weight[_]]=True
    dic = new_dic

n = int(input())
check_list = list(map(int,input().split()))
result = []
for x in check_list:
    if x in dic.keys(): result.append("Y")
    else: result.append("N")
print(*result)