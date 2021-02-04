import sys
input = sys.stdin.readline
while True:
    _ = input().rstrip('\n')
    if len(_) == 1 and _[0] == '.': break

    lst = []
    ok = True
    for data in _:
        if data not in "[]()": continue

        if data in "[(": lst.append(data)
        else:
            if len(lst) != 0 and ((lst[-1] == '[' and data == ']') or (lst[-1] == '(' and data == ')')) :
                lst.pop()
            else:
                ok = False
                break

    if not ok or len(lst) != 0: print("no")     
    else: print("yes")