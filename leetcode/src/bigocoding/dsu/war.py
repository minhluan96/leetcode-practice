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
    ended = False

    N = int(input())

    parent = [i for i in range(2 * N)]
    ranks = [0 for _ in range(2 * N)]

    while True:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            break
        else:
            if a == 1:
                '''a va b dang noi trai phia ~> co nghia la ke thu'''
                if findSet(c) == findSet(b + N):
                    print(-1)
                else:
                    unionSet(c, b)
                    unionSet(c + N, b + N)
            elif a == 2:
                if findSet(b) == findSet(c):
                    print(-1)
                else:
                    unionSet(b, c + N)
                    unionSet(c + N, c)
            elif a == 3:
                if findSet(b) == findSet(c):
                    print(1)
                else:
                    print(0)
            else:
                if findSet(b) == findSet(c + N):
                    print(1)
                else:
                    print(0)