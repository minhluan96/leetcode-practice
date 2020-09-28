class Solution:
    def george_and_round(self, n, m, requirements, prepares):
        i, j = 0, 0

        while i < n and j < m:
            if prepares[j] >= requirements[i]:
                i += 1
            j += 1
        
        return n - i
    

firstLine = list(map(int, input().split()))
n = firstLine[0]
m = firstLine[1]
requirements = list(map(int, input().split()))
prepares = list(map(int, input().split()))

n = 20
m = 25
requirements = [30,32,34,39,42,43,45,46,47,48,52,55,56,57,58,59,60,65,67,69]
prepares = [2,3,4,5,8,9,14,16,18,20,24,27,29,30,34,35,36,37,40,41,42,43,44,45,46]

n = 3
m = 5
requirements = [1,2,3]
prepares = [1,2,2,3,3]

n = 3
m = 5
requirements = [1,2,3]
prepares = [1,1,1,1,1]

n = 3
m = 1
requirements = [2,3,4]
prepares = [1]

solution = Solution()
result = solution.george_and_round(n, m, requirements, prepares)
print(result)

 