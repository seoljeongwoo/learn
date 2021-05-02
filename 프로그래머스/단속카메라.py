def solution(routes):
    answer = 0
    lst = []
    SZ = len(routes)
    camera = [0]*SZ
    
    for index, route in enumerate(routes):
        lst.append((route[0] , 0 , index))
        lst.append((route[1] , 1 , index))
        
    lst.sort()
    i , j =0, 0
    while j<len(lst):
        if lst[j][1] == 1 and camera[lst[j][2]] == 0:
            camera_cnt = 0
            for index in range(i,j+1):
                if camera[lst[index][2]] == 1: continue
                camera[lst[index][2]] = 1
                camera_cnt += 1
            i = j+1
            if camera_cnt > 0 : 
                answer += 1
        j+=1
    
    return answer
