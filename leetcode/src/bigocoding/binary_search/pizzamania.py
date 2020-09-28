import bisect


if __name__ == '__main__':
    t = int(input())

    while t > 0:
        n, m = map(int, input().split())

        budgets = list(map(int, input().split()))
        budgets.sort()
        counter = {}

        for i in range(len(budgets)):
            b = budgets[i]
            leftover = m - b
            pos = bisect.bisect_left(budgets, leftover, 0, len(budgets))
            if pos < len(budgets) and budgets[pos] + b == m and pos != i:
                if b not in counter and budgets[pos] not in counter:
                    counter[b] = budgets[pos]

        print(len(counter))

        t -= 1