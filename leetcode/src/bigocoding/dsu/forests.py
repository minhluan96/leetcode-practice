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


def hasSameOpinion(opinions1, opinions2):
    for i in range(T + 1):
        if opinions1[i] != opinions2[i]:
            return False
    return True

if __name__ == '__main__':
    TC = int(input())

    input()
    for case in range(TC):

        P, T = map(int, input().split())

        parent = [i for i in range(P + 1)]
        ranks = [0 for _ in range(P + 1)]
        opinions = [[False for _ in range(T + 1)] for _ in range(P + 1)]

        while True:
            try:
                pair = input()
                if pair == '':
                    break
                p, t = map(int, pair.split())
                opinions[p][t] = True
            except EOFError:
                break

        for i in range(1, P):
            for j in range(i + 1, P + 1):
                if hasSameOpinion(opinions[i], opinions[j]):
                    unionSet(i, j)

        for i in range(1, P + 1):
            findSet(i)

        parentSet = set(parent[1:])
        print(len(parentSet))
        if case != TC - 1:
            print()
