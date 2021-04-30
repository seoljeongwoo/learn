def solution(n, s):
    answer = [s//n]*n
    s -= sum(answer)
    index = n-1
    while s:
        answer[index] += 1
        index -= 1
        if index == -1: index += n
        s -= 1
    if 0 in answer: answer = [-1]
    return answer
