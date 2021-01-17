S = input()
C = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for data in C:
    if data in S:
        S = S.replace(data,"1")
print(len(S))