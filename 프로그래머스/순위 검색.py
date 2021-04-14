from bisect import bisect_left
def solution(info, query):
    answer = []
    num = dict()
    num["cpp"] = 0; num["java"] = 1; num["python"] = 2
    num["backend"] = 0; num["frontend"] = 1
    num["junior"] = 0; num["senior"] = 1
    num["chicken"] = 0; num["pizza"] = 1
    
    dp = [[[[0 for i in range(2)] for j in range(2)] for k in range(2)] for l in range(3)]
    
    for i in range(3):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    dp[i][j][k][l] = []
                    
    for detail in info:
        target = []
        for data in list(detail.split()):
            if data in num.keys(): target.append(num[data])
            else: target.append(int(data))
        dp[target[0]][target[1]][target[2]][target[3]].append(target[4])
    
    for i in range(3):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    dp[i][j][k][l].sort()
                    
    for detail in query:
        detail = detail.replace("and","")
        target = []
        for index, data in enumerate(list(detail.split())):
            if data == '-':
                if index ==0 : target.append((0,3))
                else: target.append((0,2))
            else:
                if data in num.keys(): target.append((num[data],num[data]+1))
                else: target.append(int(data))
        ret = 0
        for i in range(target[0][0],target[0][1]):
            for j in range(target[1][0], target[1][1]):
                for k in range(target[2][0], target[2][1]):
                    for l in range(target[3][0], target[3][1]):
                        idx = bisect_left(dp[i][j][k][l],target[4])
                        ret += len(dp[i][j][k][l]) - idx
        answer.append(ret)
        
    return answer
