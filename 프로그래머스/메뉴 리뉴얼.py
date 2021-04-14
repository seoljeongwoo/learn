from itertools import combinations
def solution(orders, course):
    answer = []
    edge = [ dict() for i in range(max(course)+1)]
    max_value = [0]*(max(course)+1)
    for order in orders:
        lst = list(order)
        lst.sort()
        for course_number in course:
            for data in list(combinations(lst,int(course_number))):
                key = ""
                for alpha in data: 
                    key+=alpha
                if key in edge[course_number]: edge[course_number][key] += 1
                else: edge[course_number][key] = 1
                max_value[course_number] = max(max_value[course_number], edge[course_number][key])

    for course_number in course:
        target = max_value[course_number]
        if target < 2: continue
        for key, value in edge[course_number].items():
            if value == target: answer.append(key)

    answer.sort()
    return answer
