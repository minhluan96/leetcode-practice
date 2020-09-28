class Solution:
    def gukizAndContest(self, n, students):
        sortedStudents = sorted(students, reverse=True)

        results = []
        resultsMap = {}
        currentScore = students[0]
        higherPos = len(results)

        for i in range(n):
            if sortedStudents[i] != currentScore:
                currentScore = sortedStudents[i]
                higherPos = len(results)

            results.append(1 + higherPos)
            resultsMap[sortedStudents[i]] = 1 + higherPos

        results = []
        for i in range(n):
            results.append(resultsMap[students[i]])

        return results


# n = 3
# students = [1,3,3]

# n = 1
# students = [1]

# n = 5
# students = [3,5,3,4,5]
# [5,5,4,3]

n = int(input())
students = list(map(int, input().split()))

solution = Solution()
result = solution.gukizAndContest(n, students)
print(*result)