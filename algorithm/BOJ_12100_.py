import sys
import copy
input = sys.stdin.readline
N = int(input())
_2048 = [list(map(int,input().split())) for _ in range(N)]
result = -1
def rotate(_2048copy):
    tmp = copy.deepcopy(_2048copy)

    for i in range(N):
        for j in range(N):
            _2048copy[j][N-1-i] = tmp[i][j]
    return _2048copy 

def direction(_2048copy):
    for i in range(N):
        tmp = []
        for j in range(N):
            if _2048copy[i][j] == 0: continue
            tmp.append(_2048copy[i][j])
        
        for j in range(N):
            if len(tmp) >= 2 and tmp[0] == tmp[1]:
                _2048copy[i][j] = tmp.pop(0)*2
                tmp.pop(0)
            elif len(tmp) >=1 :
                _2048copy[i][j] = tmp.pop(0)
            else:
                _2048copy[i][j] = 0
    return _2048copy


def calc(pick):
    _2048copy = copy.deepcopy(_2048)
    global result
    for _ in range(5):
        if pick[_] == 0:    # N
            for _ in range(3):
                _2048copy = rotate(_2048copy)
            _2048copy = direction(_2048copy)
            _2048copy = rotate(_2048copy)
        elif pick[_] == 1:  # E
            for _ in range(2):
                _2048copy = rotate(_2048copy)
            _2048copy = direction(_2048copy)
            for _ in range(2):
                _2048copy = rotate(_2048copy)
        elif pick[_] == 2:  # S
            _2048copy = rotate(_2048copy)
            _2048copy = direction(_2048copy)
            for _ in range(3):
                _2048copy = rotate(_2048copy)
        else:   # W
            _2048copy = direction(_2048copy)
    
    for data in _2048copy:
        result = max(result, max(data))
    return

def dfs(pick):
    if len(pick) == 5:
        calc(pick)
        return
    for i in range(4):
        pick.append(i)
        dfs(pick)
        pick.pop()
    return

dfs([])
print(result)