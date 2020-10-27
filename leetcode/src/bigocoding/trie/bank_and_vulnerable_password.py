class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


def addWord(root, s):
    temp = root
    for c in s:
        if c not in temp.child:
            temp.child[c] = Node()
        temp = temp.child[c]

    temp.countWord += 1


def findWord(root, s):
    temp = root
    for c in s:
        if c not in temp.child:
            return False
        if temp.child[c].countWord > 0:
            return True
        temp = temp.child[c]

    return True


if __name__ == '__main__':
    N = int(input())
    root = Node()
    found = False

    for _ in range(N):
        string = input()
        if not findWord(root, string):
            addWord(root, string)
        else:
            found = True
            print('vulnerable')
            break

    if not found:
        print('non vulnerable')
