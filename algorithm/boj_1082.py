import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
pay = int(input())

check = dict()
for index in range(N-1,-1,-1):
    value = lst[index]
    if value in check.keys() : continue
    check[value] = index

dp = dict()
dp[0] = []
def compare(alist, blist):
    a_sorted = sorted(alist , reverse = True)
    b_sorted = sorted(blist , reverse = True)
    
    for i in range(len(alist)):
        if a_sorted[i] == b_sorted[i] : continue
        if a_sorted[i] > b_sorted[i]: return True
        elif a_sorted[i] < b_sorted[i] : return False
    return False

for i in range(1,pay+1):
    length = 0
    insert_list = []
    for k , v in check.items():
        if i-k >=0:
            dp_list = dp[i-k]
            dp_len = len(dp_list)
            if v !=0 or (v==0 and dp_len != 0): 
                dp_list += [v]
                dp_len += 1
            if dp_len > length:
                length = dp_len
                insert_list = dp_list
            elif dp_len == length:
                if compare(dp_list , insert_list):
                    insert_list = dp_list
    dp[i] = insert_list
if len(dp[pay]) == 0: dp[pay] = [0]
target_list = dp[pay]
target_list.sort(reverse = True)
print(''.join(map(str,target_list)))