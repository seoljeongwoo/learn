import sys
input = sys.stdin.readline

n,m = map(int,input().split())
cnt = {}
for _ in range(n):
    word = input().rstrip('\n')
    if len(word) < m: continue
    if word in cnt.keys(): cnt[word] +=1
    else: cnt[word] = 1
sort = []
for key, value in cnt.items():
    sort.append((-1*value, -1*len(key) , key))
sort.sort()
for c,l,k in sort:
    print(k)
