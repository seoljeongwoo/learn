import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
name = list(input().rstrip('\n').split())
name_edge = {}
for person in name:
    name_edge[person] = []
name.sort()
m = int(input())
outdegree = {}
edge = {}
for _ in range(m):
    child, parent = input().rstrip('\n').split()
    if parent in edge.keys(): edge[parent].append(child)
    else: edge[parent] = [child]

    if child in outdegree.keys() : outdegree[child] +=1
    else: outdegree[child] = 1

root = []
topology = deque()
for person in name:
    if person not in outdegree.keys(): 
        root.append(person)
        topology.append(person)


while topology:
    curr_person = topology.popleft()
    if curr_person in edge.keys(): child = edge[curr_person]
    else: continue

    for child_name in child:
        outdegree[child_name] -=1
        if outdegree[child_name] == 0 :
            name_edge[curr_person].append(child_name)
            topology.append(child_name)

print(len(root))
print(*root)
for person in name:
    print(person , end= " ")
    child = name_edge[person]
    child.sort()
    print(len(child) , end= " ")
    print(*child)