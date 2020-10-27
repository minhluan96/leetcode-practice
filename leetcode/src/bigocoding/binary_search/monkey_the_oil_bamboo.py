def is_qualified(k):

    for i in range(1, n):
        if steps[i] - steps[i - 1] > k:
            return False
        elif steps[i] - steps[i - 1] == k:
            k -= 1
        else:
            # continue to jump
            continue

    return True


if __name__ == '__main__':
    T = int(input())

    for case in range(T):
        n = int(input())

        steps = list(map(int, input().split()))
        steps.insert(0, 0) # the ground position

        minStep = int(1e9)

        left = 1 # the position in the rungs
        right = steps[-1]

        while left <= right:
            mid = (left + right) // 2
            if is_qualified(mid):
                minStep = mid
                right = mid - 1
            else:
                left = mid + 1

        print('Case {}: {}'.format(case + 1, minStep))


