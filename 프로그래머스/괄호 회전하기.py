def solution(s):
    answer = 0
    SZ = len(s)
    for shift in range(SZ):
        Stack = []
        
        def convert(alpha):
            if alpha in "[]": return 0
            if alpha in "{}": return 1
            return 2
        
        for index in range(SZ):
            if s[(index + shift) % SZ] in "[({":
                N = convert(s[(index + shift) % SZ])
                Stack.append(N)
            else:
                N = convert(s[(index + shift) % SZ])
                if len(Stack) == 0 or Stack[-1] != N:
                    Stack.append(N)
                    break
                Stack.pop()
        if len(Stack) == 0: answer += 1
    return answer
