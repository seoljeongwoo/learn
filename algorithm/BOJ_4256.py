import sys
input = sys.stdin.readline
T =int(input())
def search(val):
    for i in range(n):
        if inorder[i] == val:
            return i+1
for _ in range(T):
    n = int(input())
    st = []
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    incheck = [False] * (n+2)
    incheck[0] = incheck[n+1] = True
    for x in preorder:
        idx = search(x)
        incheck[idx] = True
        st.append(idx)
        while st:
            top = st[-1]
            if incheck[top-1] == True and incheck[top+1] == True:
                print(inorder[top-1],end=" ")
                st.pop()
            else: break
    while st:
        top = st[-1]
        print(inorder[top-1],end=" ")
        st.pop()
    print()
        
                