class Node:
    def __init__(self, weight=0):
        self.countWord = 0
        self.child = dict()
        self.weight = weight


def addWord(root, s):
    temp = root
    for c in s:
        if c not in temp.child:
            temp.child[c] = Node()
        temp.child[c].weight += 1
        temp = temp.child[c]

    temp.countWord += 1


def findWord(root, s):
    temp = root
    for c in s:
        if c not in temp.child:
            return 0
        temp = temp.child[c]

    return temp.weight


if __name__ == '__main__':
    n = int(input())
    root = Node()

    for _ in range(n):
        lines = input().split()

        if lines[0] == 'add':
            addWord(root, lines[1])
        else:
            weight = findWord(root, lines[1])
            print(weight)
