from collections import deque
def solution(board, moves):
    answer = 0
    SIZE = len(board)
    boardStack = [ deque() for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0: continue
            boardStack[j].append(board[i][j])
    bucket = []
    for move in moves:
        move -= 1
        if len(boardStack[move]) == 0: continue
        value = boardStack[move].popleft()
        if len(bucket) == 0: bucket.append(value)
        else:
            if bucket[-1] == value:
                answer += 2
                bucket.pop()
            else: bucket.append(value)
    return answer
