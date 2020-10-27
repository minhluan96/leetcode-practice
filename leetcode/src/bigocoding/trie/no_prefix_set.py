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
            return True
        else:
            if temp.child[c].countWord > 0:
                return False

        temp = temp.child[c]

    return False


if __name__ == '__main__':
    n = int(input())
    root = Node()
    found = False

    for _ in range(n):
        string = input()

        if findWord(root, string):
            addWord(root, string)
        else:
            found = True
            print('BAD SET')
            print(string)
            break

    if not found:
        print('GOOD SET')