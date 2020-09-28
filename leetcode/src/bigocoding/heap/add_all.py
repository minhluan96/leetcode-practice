import heapq

if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break

        min_h = list(map(int, input().split()))

        heapq.heapify(min_h)

        total = 0

        while len(min_h) > 1:
            firstTop = heapq.heappop(min_h)
            secondTop = heapq.heappop(min_h)
            nextValue = firstTop + secondTop
            total += nextValue
            heapq.heappush(min_h, nextValue)

        print(total)
