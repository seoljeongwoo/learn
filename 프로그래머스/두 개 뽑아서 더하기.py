def solution(numbers):
    answer = set()
    size = len(numbers)
    for i in range(size):
        for j in range(i+1,size):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer
