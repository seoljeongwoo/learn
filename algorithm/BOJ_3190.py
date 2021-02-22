import sys
input = sys.stdin.readline

N , K = int(input()), int(input())
apple = [list(map(int,input().split())) for _ in range(K)]
L = int(input())
direction_info = [list(input().split()) for _ in range(L)]
_map = [[4]*N for _ in range(N)]
for x,y in apple:
    _map[x-1][y-1] = 5  # 0 , 1, 2 ,3 = direction = snake_body , 4 = empty , 5 = apple
_time , direction_index = 1, 0
curr_dir , d = 0 , [(0,1) , (1,0) , (0,-1) , (-1,0)]
head_x, head_y, tail_x, tail_y = 0 , 0 , 0 , 0
_map[head_x][head_y] = curr_dir
while True:
    next_x, next_y = head_x + d[curr_dir][0] , head_y + d[curr_dir][1]
    if next_x == -1 or next_x == N or next_y ==-1 or next_y == N or (_map[next_x][next_y] !=4 and _map[next_x][next_y] != 5):
        print(_time)
        break
    
    if _map[next_x][next_y] == 4:
        pre_dir = _map[tail_x][tail_y]
        tail_next_x , tail_next_y = tail_x + d[pre_dir][0], tail_y + d[pre_dir][1]
        _map[tail_x][tail_y] = 4
        tail_x ,tail_y = tail_next_x, tail_next_y
    
    
    if len(direction_info) > direction_index and _time == int(direction_info[direction_index][0]):
        if direction_info[direction_index][1] == 'L':
            curr_dir = (curr_dir+3)%4
        else:
            curr_dir = (curr_dir+1)%4
        direction_index += 1

    head_x, head_y = next_x, next_y
    _map[head_x][head_y] = curr_dir
    _time += 1
