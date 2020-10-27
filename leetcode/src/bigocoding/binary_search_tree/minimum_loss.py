import bisect


if __name__ == '__main__':
    n = int(input())

    '''
    i: mua
    j: bán
    loss = mua - bán 
    Bán < mua ~> p[j] > p[i]
    mua trước bán ~> j < i
    '''

    lines = list(map(int, input().split()))

    minLoss = -1

    '''
    O(N^2)
    '''

    # for i in range(n):
    #     for j in range(0, i - 1):
    #         if lines[j] > lines[i]:
    #             minLoss = min(minLoss, lines[j] - lines[i])

    '''
    Cách 2
    Tìm p[j] sao cho p[j] - p[i] = min mà p[i] cố định ~> tìm p[j] min
    '''

    for i in range(n):
        j = bisect.bisect_right(lines[:i], lines[i], 0, i)
        if 0 <= j < i:
            if minLoss == -1:
                minLoss = lines[j] - lines[i]
            else:
                minLoss = min(minLoss, lines[j] - lines[i])

    print(minLoss)

