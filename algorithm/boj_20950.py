import sys
input = sys.stdin.readline

gap = int(1e9)
def bf(curr,l,r,g,b):
    global gap
    if 2<=l<=7:
        nr,ng,nb = r,g,b
        nr//=l;ng//=l;nb//=l
        nr=abs(nr-goal[0]);ng=abs(ng-goal[1]);nb=abs(nb-goal[2])
        gap = min(gap, nr+ng+nb)

    if l == 7 or curr == n: return
    if l <=6 : bf(curr+1, l+1,r+rgb[curr][0],g+rgb[curr][1],b+rgb[curr][2])
    bf(curr+1, l,r,g,b)
    return
n = int(input())
rgb = [list(map(int,input().split())) for _ in range(n)]
goal = list(map(int,input().split()))
bf(0,0,0,0,0)
print(gap)