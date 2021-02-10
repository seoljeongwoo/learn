# import sys
# input = sys.stdin.readline
# A,B,C=map(int,input().split())
# def solve(a,b):
#     if b==1: return a
#     ret = solve(a,b//2)%C
#     ret = (ret*ret)%C
#     if b%2==1: ret = (ret*a)%C
#     return ret
# print(solve(A,B)%C)

print(pow(*map(int,input().split())))