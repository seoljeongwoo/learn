def check(row, col, Queen):
    for index,data in enumerate(Queen):
        if data == col: return False
        if abs(index-row) == abs(data-col): return False
    return True

def solve(floor, Queen, limit):
    if floor == limit: return 1
    ret = 0
    for col in range(limit):
        if check(floor, col, Queen):
            ret += solve(floor+1, Queen + [col] , limit)
    return ret

def solution(n):
    answer = solve(0,[],n)
    return answer
