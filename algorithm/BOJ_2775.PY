def cal(pre):
    for i in range(1,16):
        for j in range(1,15):
            pre[i][j] = pre[i][j-1]
            if i==1 :
                pre[i][j] += j
            elif j == 1:
                pre[i][j] += 1
            else: 
                pre[i][j] += pre[i-1][j]
    return
pre = [[0]*15 for _ in range(16)]
cal(pre)
TC = int(input())
for _ in range(TC):
    k , n = int(input()) , int(input())
    print(pre[k+1][n]- pre[k+1][n-1])