import sys
sys.setrecursionlimit(202020)
def find(room, parent):
    if room not in parent.keys(): return room
    parent[room] = find(parent[room] , parent)
    return parent[room]
def solution(k, room_number):
    answer = []
    parent = dict()
    
    for room in room_number:
        if room in parent.keys():
            room = find(room, parent)
        answer.append(room)
        parent[room] = find(room+1, parent)
    return answer
