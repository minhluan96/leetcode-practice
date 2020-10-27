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


def hasSameReligion(religion1, religion2):
    for i in range(m + 1):
        if religion1[i] != religion2[i]:
            return False
    return True

if __name__ == '__main__':
    case = 1
    while True:

        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        parent = [i for i in range(n + 1)]
        ranks = [0 for _ in range(n + 1)]
        religions = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        for _ in range(m):
            x, y = map(int, input().split())
            unionSet(x, y)

        religion_dict = {}
        for i in range(1, n + 1):
            leader = findSet(i)
            if religion_dict.get(leader) is not None:
                religion_dict[leader] += 1
            else:
                religion_dict[leader] = 1

        print('Case {0}: {1}'.format(case, len(religion_dict)))
        case += 1

