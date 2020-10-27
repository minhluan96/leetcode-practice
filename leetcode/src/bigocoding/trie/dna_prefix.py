class Node:
    def __init__(self, weight=0):
        self.countWord = 0
        self.child = dict()
        self.weight = weight


def addWord(root, s):
    temp = root
    maxWeight = 0
    i = 1
    for c in s:
        if c not in temp.child:
            temp.child[c] = Node()
        temp = temp.child[c]
        temp.weight += i
        i += 1
        if temp.weight > maxWeight:
            maxWeight = temp.weight

    temp.countWord += 1
    return maxWeight


if __name__ == '__main__':
    T = int(input())

    for case in range(T):
        N = int(input())
        root = Node()

        maxLength = 0

        for _ in range(N):
            line = input()
            currentWeight = addWord(root, line)
            maxLength = max(currentWeight, maxLength)

        print('Case {}: {}'.format(case + 1, maxLength))