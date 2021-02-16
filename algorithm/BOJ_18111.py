import sys
input = sys.stdin.readline
N,M,B= map(int,input().split())
cnt = [0] *257
for _ in range(N):
    lst = list(map(int,input().split()))
    for x in lst:
        cnt[x]+=1
result_time , result_height = (float('inf') , -1)
for h in range(257):
    used_B = 0
    _time = 0
    
    for i in range(257):
        if cnt[i] == 0: continue
        if h > i:
            _time += (h-i)*cnt[i]
            used_B -= (h-i)*cnt[i]
        elif h<i:
            _time += 2*(i-h)*cnt[i]
            used_B += (i-h)*cnt[i]
    if used_B + B >= 0: 
        if result_time == _time:
            result_height = h
        elif result_time > _time:
            result_time = _time
            result_height = h
            
print(result_time , result_height)