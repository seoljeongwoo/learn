import sys
input = sys.stdin.readline

n,m = map(int,input().split())
bucket = [list(map(int,input().split())) for _ in range(n)]
clouds = [(n-1,0), (n-1,1) ,(n-2,0),(n-2,1)]
cloud_direction = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
move_cloud_direction = [(-1,-1), (-1,1), (1,-1), (1,1)]

for _ in range(m):
    d,s = map(int,input().split())
    d -= 1

    move_clouds = dict()
    for cloud in clouds:
        nx,ny = (cloud[0] + s*cloud_direction[d][0])%n, (cloud[1] + s*cloud_direction[d][1])%n
        move_clouds[(nx,ny)] = True
        bucket[nx][ny] += 1

    watercopys = []
    for move_cloud in move_clouds.keys():
        cnt = 0
        for dx, dy in move_cloud_direction:
            nx,ny = move_cloud[0] + dx, move_cloud[1] + dy
            if 0<= nx < n and 0<= ny < n:
                if bucket[nx][ny] > 0: cnt +=1
        watercopys.append((move_cloud[0], move_cloud[1] , cnt))

    for watercopy in watercopys:
        bucket[watercopy[0]][watercopy[1]] += watercopy[2]

    new_clouds = []
    for i in range(n):
        for j in range(n):
            if bucket[i][j] < 2 : continue
            if (i,j) in move_clouds.keys(): continue
            new_clouds.append((i,j))
            bucket[i][j] -= 2
    clouds = new_clouds

ret = 0
for data in bucket:
    ret += sum(data)
print(ret)
    