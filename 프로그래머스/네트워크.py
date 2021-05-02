def solution(n, computers):
    answer = 0
    
    def find(u):
        if u == parent[u] : return u
        parent[u] = find(parent[u])
        return parent[u]
    
    def merge( u , v ):
        u = find(u)
        v = find(v)
        if u == v: return 
        parent[u] = v
        return
    
    parent = [i for i in range(n)]
    for row in range(n):
        for col in range(n):
            if computers[row][col] == 1:
                merge(row,col)
    st = set()
    for i in range(n):
        st.add(find(i))
    answer = len(st)
    return answer
