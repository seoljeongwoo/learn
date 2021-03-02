import sys
input = sys.stdin.readline

T = int(input())
lst = [0]
for i in range(32):
    lst.append(2**i)
for _ in range(T):
    x = int(input())
    if x == 0:
        print(0)
        continue
    _time , j ,curr = 0 , 1 , 0
    if x>0:
        while j<len(lst):
            _time += 4*curr + lst[j] - lst[j-1]
            if x <= lst[j]:
                _time -= (lst[j] - x)
                print(_time)
                break
            curr = lst[j]
            j+=1
    else:
        x*=-1
        while j<len(lst):
            _time += curr + 3*lst[j]
            if x<= lst[j]:
                _time -= (lst[j] - x)
                print(_time)
                break
            curr= lst[j]
            j+=1

    
    