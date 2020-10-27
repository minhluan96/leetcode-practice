def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)

    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[vp] > ranks[up]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


if __name__ == '__main__':
    N, Q = map(int, input().split())

    parent = [i for i in range(N + 1)]
    ranks = [0 for _ in range(N + 1)]

    for _ in range(Q):
        A, B = map(int, input().split())
        if findSet(A) != findSet(B):
            unionSet(A, B)
        
        temp = 2