import sys
input = sys.stdin.readline
def dc(l,r):
    if l>r : return -1
    elif l==r: return h[l]
    elif l+1==r: return max(h[l],h[r],2*min(h[l],h[r]))
    mid=(l+r)//2
    ret=max(dc(l,mid),dc(mid+1,r))
    left,right=mid,mid+1
    mh = min(h[left],h[right])
    ret = max(ret, 2*mh)
    while True:
        if l < left and right < r:
            if h[left-1] < h[right+1]: right +=1; mh=min(mh,h[right])
            else: left -= 1; mh=min(mh,h[left])
        elif l==left:
            right+=1;mh=min(mh,h[right])
        elif r==right:
            left -=1;mh=min(mh,h[left])
        ret = max(ret, (right-left+1)*mh)
        if left==l and right == r: break
    return ret
n = int(input().rstrip('\n'))
h = [int(input().rstrip('\n')) for _ in range(n)]
print(dc(0,n-1))