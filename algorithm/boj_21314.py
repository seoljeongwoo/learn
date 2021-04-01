import sys
input = sys.stdin.readline

def max_n(n):
    ret = []
    index = 0
    mcount = 0
    while index < len(n):
        if n[index] == 'M': mcount +=1
        else: 
            ret.append('5')
            for _ in range(mcount): ret.append('0')
            mcount = 0
        index +=1
    if mcount !=0 :
        for _ in range(mcount): ret.append('1')
    print(''.join(map(str,ret))) 

def min_n(n):
    ret = []
    for index in range(len(n)):
        if index ==0:
            if n[index] == 'M': ret.append('1')
            else: ret.append('5')
            continue
        if n[index] == 'K': ret.append('5')
        else:
            if n[index-1] == 'M': ret.append('0')
            else: ret.append('1')
    print(''.join(map(str,ret)))
        
s = list(input().rstrip('\n'))
max_n(s)
min_n(s)