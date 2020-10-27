if __name__ == '__main__':
    n, k = map(int, input().split())

    numbers = list(map(int, input().split()))
    numbers.sort()

    counter = 0

    for num in numbers:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] - k == num:
                counter += 1
                break
            elif numbers[mid] - num > k:
                right = mid - 1
            else:
                left = mid + 1

    print(counter)