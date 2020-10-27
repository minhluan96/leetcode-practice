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
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


if __name__ == '__main__':

    n, m = map(int, input().split())

    parent = [i for i in range(n + 1)]
    ranks = [0 for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        unionSet(u, v)

    countSet = 0
    for i in range(1, n + 1):
        if i == parent[i]:
            countSet += 1

    if m == n and countSet == 1:
        print('FHTAGN!')
    else:
        print('NO')