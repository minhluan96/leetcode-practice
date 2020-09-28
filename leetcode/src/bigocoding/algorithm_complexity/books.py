class Solution:
    def maximumBooks(self, n, t, times):
        windowStart = 0
        totalTime = 0
        maxTime = 0
        endPos = 0

        for windowEnd in range(n):
            totalTime += times[windowEnd]
            endPos = windowEnd
            if totalTime >= t:
                maxTime = max(maxTime, totalTime)
                totalTime -= times[windowStart]
                windowStart += 1
            
        
        return len(times[windowStart:endPos + 1])

firstLine = list(map(int, input().split()))
n = firstLine[0]
t = firstLine[1]
times = list(map(int, input().split()))
solution = Solution()
result = solution.maximumBooks(n, t, times)
print(result)

