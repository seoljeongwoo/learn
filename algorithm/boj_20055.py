import sys
input = sys.stdin.readline

n,k = map(int,input().split())
lst = list(map(int,input().split()))
size = 2*n
used = [False]*n
turn =1
z_cnt = 0 
while True:

    # move
    new_lst = [0]*size
    for i in range(size):
        new_lst[(i+1)%size] = lst[i]
    lst = new_lst
    new_used = [False]*n

    for i in range(n-2,-1,-1):
        new_used[i+1] = used[i]
    new_used[n-1] = False
    used = new_used

    for i in range(n-2,-1,-1):
        if used[i] == True and used[i+1] ==False and lst[(i+1)%size] >0 :
            used[i+1], used[i] = True, False
            lst[(i+1)%size]-= 1
            if lst[(i+1)%size] == 0: z_cnt +=1
    
    used[n-1] = False

    if used[0]== False and lst[0] > 0:
        used[0] = True; lst[0] -=1
        if lst[0] == 0: z_cnt +=1
    
    if z_cnt >= k: break
    turn +=1
print(turn)