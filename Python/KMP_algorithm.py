def getpi(pattern):
    P = len(pattern)
    _next ,i , j = [] , 0, -1
    while i<P:
        _next.append(j)
        while j>=0 and pattern[i] != pattern[j] : j = _next[j]
        i+=1
        j+=1
    return _next

def KMP_search(text , pattern):
    _next = getpi(pattern)
    T = len(text)
    P = len(pattern)
    i, j = 0 , 0
    while i<T:
        while j>=0 and text[i] != pattern[j]: j = _next[j]
        i+=1
        j+=1
        if j==P:
            return i-P
    return -1
text = "asdjklasjdklasdjklasjdsioadjioqwemqnmnqwjkehqwuiqwe"
pattern = "jioqwe"
print(KMP_search(text,pattern))