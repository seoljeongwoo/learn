import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
one = 0
for data in lst:
    if data == 1: one += 1

if one == n:
    print("koosaga" if n%2 == 0 else "cubelover")
else:
    if one > 0 and one % 2 == 0:
        for data in lst:
            if data > 1: 
                data = 1
                break
    answer = 0
    for data in lst:
        answer ^= data
        
    print("koosaga" if answer > 0 else "cubelover")
