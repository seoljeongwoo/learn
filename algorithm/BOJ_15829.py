import sys
input = sys.stdin.readline
n,s=int(input()), input()
result = 0 
for i in range(n):
    result = (result + (ord(s[i])-ord('a') +1)*pow(31,i,1234567891))%1234567891
print(result)
