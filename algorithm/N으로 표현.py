def solution(N, number):
    answer = -1
    s = [ set() for _ in range(9)]
    for index in range(1,9): s[index].add(int(str(N)*index))
    for i in range(1,9):    
        for j in range(1,i):
            for val1 in s[j]:
                for val2 in s[i-j]:
                    s[i].add(val1 + val2)
                    s[i].add(val1 - val2)
                    s[i].add(val1 * val2)
                    if val2 != 0: s[i].add(val1 // val2)
        if number in s[i]:
            answer = i
            break
    return answer
