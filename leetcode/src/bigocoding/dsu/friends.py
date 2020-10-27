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
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        parent = [i for i in range(N + 1)]
        ranks = [0 for _ in range(N + 1)]

        for _ in range(M):
            a, b = map(int, input().split())
            unionSet(a, b)

        for i in range(1, N + 1):
            findSet(i)

        maxGroup = 0
        parentMap = {}
        for num in parent:
            if num not in parentMap:
                parentMap[num] = 0
            parentMap[num] += 1

        for k, v in parentMap.items():
            maxGroup = max(maxGroup, v)

        print(maxGroup)