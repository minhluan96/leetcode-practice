class Solution:
    def towers(self, n, bars):
        total = len(set(bars))

        bars.sort(reverse=True)

        numFrequency = {}

        for i in range(n):
            if bars[i] not in numFrequency:
                numFrequency[bars[i]] = 0
            numFrequency[bars[i]] += 1

        maxValue = 0

        for key, value in numFrequency.items():
            if maxValue < value:
                maxValue = value

        return [maxValue, total]


# n = 3
# bars = [1,2,3]

# n = 4
# bars = [6,5,6,7]

n = int(input())
bars = list(map(int, input().split()))

solution = Solution()
result = solution.towers(n, bars)
print(*result)
