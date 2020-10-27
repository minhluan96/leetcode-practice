if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())

        candles = list(map(int, input().split()))

        before = candles[:N]
        beforeSet = set(before)

        after = candles[N:]

        for c in after:
            if c in beforeSet:
                print('YES')
            else:
                print('NO')
            beforeSet.add(c)

