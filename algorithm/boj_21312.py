import sys
input = sys.stdin.readline

def compare(x,y):
    if x%2 == y%2:
        if x<=y: return False
        else: return True
    else:
        if x%2 ==1: return True
        else : return False
a,b,c = map(int,input().split())
lst = []
lst.append(a);lst.append(b);lst.append(c)
lst.append(a*b);lst.append(a*c);lst.append(b*c)
lst.append(a*b*c)
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if compare(lst[i], lst[j]):
            lst[i], lst[j] = lst[j] , lst[i]
print(lst[-1])