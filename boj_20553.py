import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input())-1 for _ in range(n)]
ok = [False] * n
for i in range(n):
    st = [i]
    target = lst[i]
    while True:
        if target in st: st.append(target); break
        st.append(target); target = lst[target]
    if st[-1] == i:
        while st:
            ok[st.pop()] = True
ret = []
for index, data in enumerate(ok):
    if data == True: ret.append(index+1)
print(len(ret))
for data in ret: print(data)