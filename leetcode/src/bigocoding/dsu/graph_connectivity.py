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

    for o in range(T):
        if o == 0:
            input()

        largestNodeName = input()
        ALPHABET = 26
        N = ord(largestNodeName) - ord('A') + 1
        parent = [i for i in range(N)]
        ranks = [0 for _ in range(N)]

        while True:
            try:
                pairs = input()
                if pairs == '':
                    break
                a, b = pairs[0], pairs[1]
                aPos = ord(a) - ord('A')
                bPos = ord(b) - ord('A')

                unionSet(aPos, bPos)
            except EOFError:
                break

        for i in range(N):
            findSet(i)

        parentsMap = set(parent)
        print(len(parentsMap))
        if o != T - 1:
            print()

