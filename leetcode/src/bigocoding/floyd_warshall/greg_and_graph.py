class Solution:
    def greg_and_graph(self):
        for r in range(N):
            k = x[id]
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


        for i in range(id, N):
            for j in range(id, N):
                res[id] += dist[x[i]][x[j]]

        for in range(N):
            print(res[i])


if __name__ == '__main__':
    N = int(input())

    for i in range(N):
        for j in range(N):
            v = int(input())
            dist[i][j] = v

    for i in range(N):
        x = int(input())
        remover.append(x)


    res = []




