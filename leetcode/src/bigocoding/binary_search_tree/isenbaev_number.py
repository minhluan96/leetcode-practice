import queue
import collections


def bfs(start):
    visited = n * 3 * [False]
    dist = n * 3 * [-1]

    q = queue.Queue()

    visited[start] = True
    dist[start] = 0
    q.put(start)

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.put(v)

    return dist


if __name__ == '__main__':
    n = int(input())

    pos = 0
    nameMap = {}
    graph = [[] for i in range(n * 3)]

    for i in range(n):
        s1, s2, s3 = list(input().split())
        if s1 not in nameMap:
            nameMap[s1] = pos
            pos += 1
        if s2 not in nameMap:
            nameMap[s2] = pos
            pos += 1
        if s3 not in nameMap:
            nameMap[s3] = pos
            pos += 1

        t, u, v = nameMap[s1], nameMap[s2], nameMap[s3]
        graph[t].append(u)
        graph[t].append(v)

        graph[u].append(t)
        graph[u].append(v)

        graph[v].append(t)
        graph[v].append(u)

    odNameMap = collections.OrderedDict(sorted(nameMap.items()))
    dist = bfs(nameMap['Isenbaev'])

    for k, v in odNameMap.items():
        if dist[v] == -1:
            print('{} undefined'.format(k))
        else:
            print('{} {}'.format(k, dist[v]))