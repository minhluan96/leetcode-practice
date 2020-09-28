def is_qualified(trees, max_value, n, k):
    total_parts = 0

    for i in range(n):
        tree = trees[i]
        if tree > max_value:
            total_parts += tree - max_value

    return total_parts >= k


if __name__ == '__main__':
    N, M = map(int, input().split())

    trees = list(map(int, input().split()))

    trees.sort()

    left = 0
    right = trees[-1]

    while left < right - 1:
        mid = (left + right) // 2
        if is_qualified(trees, mid, N, M):
            left = mid
        else:
            right = mid

    print(left)

