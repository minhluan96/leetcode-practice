class Node:
    def __init__(self):
        self.child = [None, None]
        self.blocked = False
        self.parent = None

def addWord(root, word):
    length = 1
    id = 0
    temp = root
    stringArr = ['0'] * word[length]
    i = 0

    while i < word[length]:
        nextChar = -1
        for j in range(2):
            if temp.child[j] is None or not temp.child[j].blocked:
                nextChar = j
                break

        if nextChar == -1:
            if temp == root:
                return False

            temp.blocked = True
            temp = temp.parent
            i -= 1
        else:
            if temp.child[nextChar] is None:
                temp.child[nextChar] = Node()
                temp.child[nextChar].parent = temp

            temp = temp.child[nextChar]
            if nextChar == 0:
                stringArr[i] = '0'
            else:
                stringArr[i] = '1'

            i += 1

    temp.blocked = True
    ans[word[id]] = ''.join(stringArr)
    return True

'''
Time complexity O(N * l)
'''
if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    ans = [''] * N
    root = Node()

    numsFrequency = {}
    for i in range(N):
        numsFrequency[i] = nums[i]

    sortedNumsMap = {k: v for k, v in sorted(numsFrequency.items(), key=lambda item: item[1])}
    found = False
    for k, v in sortedNumsMap.items():
        if not addWord(root, (k, v)):
            found = False
            print('NO')
            break
        else:
            found = True
    if found:
        print('YES')
        for i in range(N):
            print(ans[i])
