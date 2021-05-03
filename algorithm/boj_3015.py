import sys
input = sys.stdin.readline

Stack = []
N = int(input())
answer = 0
for _ in range(N):
    h = int(input())
    if len(Stack) == 0:
        Stack.append([h,1])
        continue
    if Stack[-1][0] > h:
        answer += 1
        Stack.append([h,1])
    elif Stack[-1][0] == h:
        answer += Stack[-1][1]
        Stack[-1][1] += 1
        if len(Stack) > 1: answer += 1
    elif Stack[-1][0] < h:
        while len(Stack) > 0 and Stack[-1][0] < h:
            answer += Stack[-1][1]
            Stack.pop()
        if len(Stack) > 0 and Stack[-1][0] == h: 
            answer += Stack[-1][1]
            Stack[-1][1] += 1
            if len(Stack) > 1: answer += 1
        elif len(Stack) > 0 and Stack[-1][0] > h:
            answer += 1
            Stack.append([h,1])
        elif len(Stack) == 0:
            Stack.append([h,1])
print(answer)
