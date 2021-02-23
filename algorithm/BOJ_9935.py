import sys
input = sys.stdin.readline
_input , Bomb = input().rstrip('\n'), input().rstrip('\n')
lBomb = list(Bomb)
l = len(Bomb)
Stack = []
for data in _input:
    Stack.append(data)
    if Bomb[-1] == data and Stack[-l:] == lBomb:
        del Stack[-l:]
print(''.join(Stack) if Stack else "FRULA")