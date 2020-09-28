class Solution:
    def chores(self, n, a, b, complexity):
        complexity.sort()
        return complexity[b] - complexity[b - 1]

n = 5
a = 2
b = 3
complexity = [6,2,3,100,1]
[1,2,3,6,100]

# n = 7
# a = 3
# b = 4
# complexity = [1,1,9,1,1,1,1]

# firstLine = list(map(int, input().split()))
# n = firstLine[0]
# a = firstLine[1]
# b = firstLine[2]
# complexity = list(map(int, input().split()))

solution = Solution()
result = solution.chores(n, a, b, complexity)
print(result)