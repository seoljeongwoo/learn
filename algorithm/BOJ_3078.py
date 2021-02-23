import sys
input = sys.stdin.readline
N,K=map(int,input().split())
result = 0
name_length = [0]*21
Friend = [input().rstrip('\n') for _ in range(N)]
i, j = 0, 0
while j<K:
    curr_len = len(Friend[j])
    result += name_length[curr_len]
    name_length[curr_len] += 1
    j+=1
while True:
    if j>= len(Friend): break
    j_len = len(Friend[j])
    result += name_length[j_len]
    name_length[j_len] += 1
    j+=1

    i_len = len(Friend[i])
    name_length[i_len] -= 1
    i+=1

print(result)