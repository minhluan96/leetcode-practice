from string import ascii_lowercase

class Node:
    def __init__(self):
        self.child = dict()
        self.countWord = 0


def addWord(root, word, side):
    temp = root
    for i in range(len(word)):
        c = word[i]
        if c not in temp.child:
            temp.child[c] = Node()
            if i > 0:
                count[side][c] += 1

        temp = temp.child[c]



if __name__ == '__main__':
    '''
    Bước 1: Số lượng toàn bộ = Số lượng prefix * số lượng suffix
    Số lượng prefix có thể tính được bằng Trie (số node của cây)

    Bước 2: Tính số lượng trùng:
    Số lượng trùng nhau = sum(số lượng prefix kết thúc là c * số lượng suffix bắt đầu bằng c)
    c chạy từ a ... z
    '''
    P, S = map(int, input().split())
    ALPHABET = 26
    SIDE = 2
    root = Node()
    count = [[0] * ALPHABET] * SIDE
    for i in range(P):
        string = input()
        addWord(root, string, 0)

    for i in range(S):
        string = input()
        reverseStr = string[::-1]
        addWord(root, reverseStr, 1)

    res = 0
    countPrefix = 0
    countSuffix = 0

    for c in ascii_lowercase:
        countPrefix += count[0][c]
        countSuffix += count[1][c]
        res -= count[0][c] * count[1][c]

    res += countPrefix * countSuffix
    print(res)

