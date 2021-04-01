import sys
input = sys.stdin.readline
def get_num(s):
    if 'a'<=s<='z': return ord(s)-ord('a')+10
    else : return ord(s) - ord('0')

def val(st , digit):
    ss = 0
    size = len(st)
    for index in range(size-1,-1,-1):
        ss += get_num(st[index])*(digit**(size-1-index))
    if ss >= INF : return -1
    else : return ss

INF = (1<<63)
x,y = input().rstrip('\n').split()

ret = 0
posvalue , adigit, bdigit = 0,0,0
xs , ys = 0,0
for data in x: xs = max(xs,get_num(data))
for data in y: ys = max(ys,get_num(data))
for row in range(xs+1, 37):
    xvalue = val(x,row)
    if xvalue == -1: continue
    for col in range(ys+1, 37):
        if row == col: continue
        yvalue = val(y,col)
        if yvalue == -1: continue
        if xvalue == yvalue: 
            ret +=1
            posvalue , adigit, bdigit = xvalue, row, col

if ret ==0 : print("Impossible")
elif ret >1 : print("Multiple")
else: print(posvalue, adigit, bdigit)