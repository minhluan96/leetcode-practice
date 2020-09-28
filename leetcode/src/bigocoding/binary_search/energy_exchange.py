def accumulate(bottles, average, k):
    lost = 0
    receive = 0

    for b in bottles:
        if b > average:
            decreased = b - average
            lost += decreased - ((decreased * k) / 100)
        else:
            receive += average - b

    return lost >= receive


if __name__ == '__main__':
    n, k = map(int, input().split())

    bottles = list(map(int, input().split()))
    bottles.sort()

    low = 0
    high = bottles[-1]

    while high - low > 1e-7:
        mid = (low + high) / 2

        if accumulate(bottles, mid, k):
            low = mid
        else:
            high = mid

    print('{0:.9f}'.format(low))
