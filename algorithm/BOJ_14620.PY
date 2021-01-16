import sys
input = sys.stdin.readline
N = int(input())
direction = [(0,1),(0,-1),(1,0),(-1,0)]
result = 1e9
def plus(flower, x, y):
    ret = flower[x][y]
    for dx, dy in direction:
        ret += flower[x+dx][y+dy]
    return ret

def bf(flower, count, total,visited):
    global result
    if total >= result:
        return

    if count == 3:
        result = min(result, total)
        return

    for i in range(N):
        for j in range(N):
            if visited[i][j] == True:
                continue
            ok = 0

            for dx , dy in direction:
                nx ,ny = i+dx,j+dy
                if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False:
                    ok+=1

            if ok == 4:
                for dx,dy in direction:
                    nx,ny = i+dx,j+dy
                    visited[nx][ny] = True
                visited[i][j] = True

                _sum = plus(flower,i,j)

                bf(flower,count+1,total+_sum,visited)

                visited[i][j] = False
                for dx,dy in direction:
                    nx,ny = i+dx, j+dy
                    visited[nx][ny] = False
    return

flower ,visited = [] , [ [False]*N for _ in range(N)]
for _ in range(N):
    flower.append(list(map(int,input().split())))

bf(flower,0,0,visited)
print(result)