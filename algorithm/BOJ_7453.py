import sys
input = sys.stdin.readline

N = int(input())
Arr = [ list(map(int,input().split())) for _ in range(N)]
AB , CD = [] , []
for i in range(N):
    for j in range(N):
        AB.append(Arr[i][0] + Arr[j][1])
        CD.append(Arr[i][2] + Arr[j][3])
AB.sort()
CD.sort()
i, j= 0, len(CD)-1
result = 0
while i<len(AB) and j>=0:
    if AB[i] + CD[j] == 0:
        nexti,nextj=i+1,j-1
        while nexti < len(AB) and AB[i] == AB[nexti]:
            nexti+=1
        while nextj >=0 and CD[j] == CD[nextj]:
            nextj-=1

        result += (nexti-i) * (j-nextj)
        i ,j = nexti, nextj

    elif AB[i] + CD[j] > 0:
        j-=1
    else:
        i+=1
print(result)