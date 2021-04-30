def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    ns = []
    for data in s: ns.append(data.split(','))
    ns.sort( key = len)
    used = dict()
    for data in ns:
        for num in data:
            if num not in used.keys(): 
                answer.append(int(num))
                used[num] = True
    return answer
