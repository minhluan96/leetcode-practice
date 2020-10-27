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

def hasSameLanguage(lanugage1, language2):
    for i in range(m + 1):
        if lanugage1[i] != language2[i]:
            return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    ranks = [0 for _ in range(n + 1)]
    languagues = [[False for _ in range(m + 1)] for _ in range(n + 1 )]

    for i in range(n):
        lines = list(map(int, input().split()))
        numberLanguages = lines[0]
        if numberLanguages == 0:
            continue
        for l in lines[1:]:
            languagues[i + 1][l] = True

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            for k in range(m + 1):
                if languagues[i][k] == True and languagues[j][k] == True:
                    unionSet(i, j)

    language_dict = {}
    for i in range(1, n + 1):
        leader = findSet(i)
        if language_dict.get(leader) is not None:
            language_dict[leader] += 1
        else:
            language_dict[leader] = 1


    count = 0
    maxGroup = max(language_dict.values())
    if maxGroup == n:
        print(count)
    else:
        print(len(set(parent[1:])) -1)



