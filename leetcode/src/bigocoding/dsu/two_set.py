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
    n, a, b = map(int, input().split())

    A = n + 1
    B = A + 1

    parent = [i for i in range(n + 3)]
    ranks = [0 for _ in range(n + 3)]
    numMap = {}
    numList = list(map(int, input().split()))

    for i in range(n):
        numMap[numList[i]] = i

    for i in range(n):
        if (a - numList[i]) in numMap:
            unionSet(i, numMap[a - numList[i]])
        else:
            unionSet(i, B)

        if (b - numList[i]) in numMap:
            unionSet(i, numMap[b - numList[i]])
        else:
            unionSet(i, A)

    if findSet(A) == findSet(B):
        print('NO')
    else:
        print('YES')
        for i in range(n):
            ''' Added 2 because the extensions of A = n + 1 and B = A + 1 '''
            if findSet(i) == findSet(n + 2):
                print(1, end=' ')
            else:
                print(0, end=' ')
