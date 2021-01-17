N,M,unused = int(input()), int(input()), list(map(int,input().split()))
used = [ i for i in range(10)]

for i in unused:
    used.remove(i)
click = abs(N-100)
for i in range(1000001):
    ok = True
    j = str(i)
    if click < len(j):
        continue

    for _j in j:
        if int(_j) not in used:
            ok = False
            break
    if ok == False:
        continue
    click = min(click, len(j) + abs(i-N))
    
print(click)
            
