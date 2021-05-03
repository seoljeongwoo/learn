import sys
input = sys.stdin.readline

s = list(input().rstrip('\n'))
mul , answer = 1, 0
Stack = []
for index, data in enumerate(s):
    if data == '(':
        mul *= 2
        Stack.append('(')
    elif data == '[':
        mul *= 3
        Stack.append('[')
    elif data == ')':
        if len(Stack) == 0 or Stack[-1] != '(':
            Stack.append(1); break
        if s[index-1] == '(': answer += mul
        mul //= 2
        Stack.pop()
    elif data == ']':
        if len(Stack) == 0 or Stack[-1] != '[':
            Stack.append(1); break
        if s[index-1] == '[': answer += mul
        mul //= 3
        Stack.pop()
print(answer if len(Stack) == 0 else 0)
