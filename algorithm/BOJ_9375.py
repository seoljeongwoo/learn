import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    N = int(input())
    dic = dict()
    for __ in range(N):
        clothes , category = input().rstrip('\n').split(' ')
        if category not in dic.keys(): dic[category] = 1
        else: dic[category] += 1 
   
    result = 1
    for key, value in dic.items():
        result *= (value+1)
    
    print(result-1)
