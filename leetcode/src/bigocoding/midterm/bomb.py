class Cell:
    def __init__(self):


class Solution:
    def bomb(self):
        pass

if __name__ == '__main__':
    R, C = list(map(int, input().split()))
    k = int(input())

    graph = [[] for _ in range(R)]

    for i in range(C):
        lines = list(map(int, input().split()))
        pos = lines[0]
        numBombs = lines[1]
        for j in numBombs:
            graph[pos].append((j, 1))