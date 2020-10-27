# BLUE_LEC18P01


def solution():
    N = int(input())

    tasks = list(map(int, input().split()))

    markers = {}

    for i in range(N):
        if markers.get(tasks[i]) is None:
            markers[tasks[i]] = [1]
        markers[tasks[i]].append(i)

    possible = False
    possible_count = 1

    duplications = []
    duplicated_keys = []
    for key, marker in markers.items():
        if len(marker) == 3:
            possible_count *= 2
            duplications.append(marker)
            duplicated_keys.append(key)
            if possible_count >= 3:
                possible = True
                break

        elif len(marker) >= 4:
            possible = True
            duplications = [marker]
            duplicated_keys = [key]
            break

    if not possible:
        print('NO')
        return

    print('YES')
    tasks.sort()

    if len(duplications) == 2:

        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1
        markers[duplicated_keys[0]][2], markers[duplicated_keys[0]][1] = markers[duplicated_keys[0]][1], \
                                                                         markers[duplicated_keys[0]][2]

        for marker in markers.values():
            marker[0] = 1
        print()
        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1
        for marker in markers.values():
            marker[0] = 1
        print()

        markers[duplicated_keys[1]][2], markers[duplicated_keys[1]][1] = markers[duplicated_keys[1]][1], \
                                                                         markers[duplicated_keys[1]][2]

        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1

    if len(duplications) == 1:
        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1

        print()
        for marker in markers.values():
            marker[0] = 1
        markers[duplicated_keys[0]][2], markers[duplicated_keys[0]][1] = markers[duplicated_keys[0]][1], \
                                                                         markers[duplicated_keys[0]][2]

        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1

        print()
        for marker in markers.values():
            marker[0] = 1
        markers[duplicated_keys[0]][2], markers[duplicated_keys[0]][3] = markers[duplicated_keys[0]][3], \
                                                                         markers[duplicated_keys[0]][2]

        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1


solution()


# BLUE_LEC18P02
import math


def solution():
    T = int(input())

    for i in range(T):
        second = int(input())

        sqrt = math.ceil(math.sqrt(second))
        r = sqrt * sqrt - second
        if r < sqrt:
            y = r + 1
            x = sqrt
        else:
            x = 2 * sqrt - r - 1
            y = sqrt

        if sqrt % 2 == 1:
            x, y = y, x

        print("Case {0}: {1} {2}".format(i + 1, x, y))


solution()


# BLUE_LEC18P03

parent = []
ranks = []


def make_set(N):
    global parent, ranks
    parent = [i for i in range(N + 5)]
    ranks = [0 for i in range(N + 5)]


def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]


def union_set(u, v):
    up = find_set(u)
    vp = find_set(v)

    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


def has_same_opinion(opinions1, opinions2, length):
    for i in range(length):
        if opinions1[i] != opinions2[i]:
            return False
    return True


def solution():

    t = 1
    while True:
        n, m = map(int, input().split())
        if m == 0 and n == 0:
            break

        make_set(n)

        for i in range(m):
            x, y = map(int, input().split())
            union_set(x, y)

        religion_leaders = dict()

        for i in range(1, n + 1):
            leader = find_set(i)
            if religion_leaders.get(leader) is not None:
                religion_leaders[leader] += 1
            else:
                religion_leaders[leader] = 1

        print("Case {0}: {1}".format(t, len(religion_leaders)))
        t += 1


solution()


# BLUE_LEC18P0o4
import math


class Triad:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        return str(self.source) + '-' + str(self.target) + ': ' + str(self.weight)


parent = []
ranks = []
dist = []
graph = []


def make_set(V):
    global parent, ranks, dist
    parent = [i for i in range(V + 1)]
    ranks = [0 for _ in range(V + 1)]


def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]


def union_set(u, v):
    up = find_set(u)
    vp = find_set(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


def kruskal(number_of_cities):
    graph.sort(key=lambda _edge: _edge.weight)
    i = 0
    mst = 0
    while len(dist) != number_of_cities - 1 and i < len(graph):
        edge = graph[i]
        i += 1
        u = find_set(edge.source)
        v = find_set(edge.target)
        if u != v:
            dist.append(edge)
            union_set(u, v)
            mst += edge.weight

    return mst


def calculate_distance(freckle1, freckle2):
    x1, y1 = freckle1
    x2, y2 = freckle2
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def solution():

    N = int(input())
    for t in range(N):
        input()
        global graph, dist
        graph = []
        dist = []
        freckles_number = int(input())
        freckles = []

        for i in range(freckles_number):
            x, y = map(float, input().split())
            freckles.append((x, y))

        for i in range(freckles_number):
            for j in range(i + 1, freckles_number):
                graph.append(Triad(i, j, calculate_distance(freckles[i], freckles[j])))

        make_set(freckles_number)

        print('%.2f' % kruskal(freckles_number))
        if t != N - 1:
            print()


solution()


# BLUE_LEC18P0o4


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


def add_word(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()
        tmp = tmp.child[ch]
        if tmp.countWord > 0:
            return False

    if len(tmp.child) > 0:
        return False
    tmp.countWord += 1
    return True


def solution():
    tc = int(input())
    for t in range(tc):
        root = Node()
        n = int(input())
        duplicated = False
        for i in range(n):
            s = input()
            result = add_word(root, s)
            if not result:
                print('NO')
                duplicated = True
                break
        if not duplicated:
            print('YES')


solution()
