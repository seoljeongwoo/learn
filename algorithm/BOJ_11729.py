
def hanoi(N, a , b):
    if N==0:
        return
    hanoi(N-1,a , 6-a-b)
    print(a,b)
    hanoi(N-1,6-a-b, b)
    return

N = int(input())
print(2**N-1)
hanoi(N,1,3)
