s = input()
N = int(s)
if N==0:
    print(1)
    exit()
cnt = [0]*10
while N:
    cnt[N%10]+=1
    N = N//10
result= max(cnt)
ns= ''
for i in range(1,len(s)+1):
    ns += '1'
    if int(ns) <= int(s):
        result= max(result, i)
print(result)