import bisect

if __name__ == '__main__':
    N = int(input())

    ladies = list(map(int, input().split()))

    Q = int(input())

    queries = list(map(int, input().split()))

    for i in range(Q):
        q = queries[i]

        pos = bisect.bisect_right(ladies, q, 0, N)

        left = 0
        right = pos - 1
        found = False

        while left <= right:
            mid = (left + right) // 2

            if q == ladies[mid]:
                found = True
                break
            elif q < ladies[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if not found:
            left -= 1
        else:
            if ladies[left] >= q:
                left -= 1

        leftVal = ladies[left] if 0 <= left < N else 'X'
        rightVal = ladies[pos] if 0 <= pos < N else 'X'

        print('{} {}'.format(leftVal, rightVal))



