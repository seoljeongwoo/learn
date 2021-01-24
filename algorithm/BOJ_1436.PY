N = int(input())
num ,cnt = 666, 0
while True:
    curr = str(num)
    if curr.count('666') >= 1: cnt += 1 
    if cnt == N: break
    num += 1
print(num)