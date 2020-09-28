class Solution:
    def devuTheDumbGuy(self, n, speed, chapters):
        chapters.sort()
        totalTime = 0

        for i in range(n):
            totalTime += chapters[i] * speed

            if speed > 1:
                speed -= 1
        
        return totalTime


firstLine = list(map(int, input().split()))
n = firstLine[0]
x = firstLine[1]
chapters = list(map(int, input().split()))


# n = 3
# x = 3
# chapters = [1,1,1]
solution = Solution()
result = solution.devuTheDumbGuy(n, x, chapters)
print(result)