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
    n = int(input())

    parent = [i for i in range(n + 1)]
    ranks = [0 for _ in range(n + 1)]
    snowDriftPair = []

    for _ in range(n):
        x, y = map(int, input().split())
        snowDriftPair.append((x, y))

    for i in range(n - 1):
        for j in range(i + 1, n):
            if snowDriftPair[i][0] == snowDriftPair[j][0] or \
                    snowDriftPair[i][1] == snowDriftPair[j][1]:
                unionSet(i, j)

    numberOfSnowDriftSet = {}
    for i in range(n):
        setSnow = findSet(i)
        if setSnow not in numberOfSnowDriftSet:
            numberOfSnowDriftSet[setSnow] = 1
        else:
            numberOfSnowDriftSet[setSnow] += 1

    '''
    Exclude the root itself
    '''
    print(len(numberOfSnowDriftSet) - 1)

