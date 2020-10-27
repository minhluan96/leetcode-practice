class Node:
    def __init__(self, weight=0):
        self.countWord = 0
        self.child = dict()
        self.weight = weight


def addWord(root, s, weight):
    temp = root
    for c in s:
        if c not in temp.child:
            temp.child[c] = Node(weight)
        else:
            temp.child[c].weight = max(temp.child[c].weight, weight)

        temp = temp.child[c]

    temp.countWord += 1


def findWord(root, s):
    temp = root
    for c in s:
        if c not in temp.child:
            return -1
        temp = temp.child[c]

    return temp.weight


if __name__ == '__main__':
    n, q = map(int, input().split())

    strMap = {}
    root = Node()

    for _ in range(n):
        line = input().split()
        strMap[line[0]] = int(line[1])
        addWord(root, line[0], int(line[1]))

    for _ in range(q):
        t = input()

        maxValue = findWord(root, t)

        print(maxValue)
