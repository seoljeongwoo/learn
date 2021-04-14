from itertools import combinations
def solution(relation):
    answer = 0
    ret = []
    for length in range(1,len(relation[0])+1):
        lst = [i for i in range(len(relation[0]))]
        ok = True
        for data in list(combinations(lst,length)):
            duplicate_check = dict()
            ok = True
            for row in relation:
                pick_lst = []
                for col in data:
                    pick_lst.append(row[col])
                key = tuple(pick_lst)
                if key in duplicate_check.keys(): ok = False
                else: duplicate_check[key] = True
            if ok: ret.append((len(data),data))
                
    check = [False]* len(ret)
    for i in range(len(ret)):
        if check[i] == True: continue
        answer += 1
        data = ret[i][1]
        for j in range(i+1, len(ret)):
            cnt = 0
            for k in data:
                if k in ret[j][1]: cnt+=1
            if cnt == len(data): check[j] = True
   

    return answer
