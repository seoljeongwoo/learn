N = int(input())
W = list(map(int,input().split()))
W.sort()
if W[0] != 1:
    print(1)
    exit()
limit = 1
for i in range(1,N):
    if W[i] <= limit+1:
        limit += W[i]
    else:
        print(limit+1)
        exit()
print(limit+1)
exit()