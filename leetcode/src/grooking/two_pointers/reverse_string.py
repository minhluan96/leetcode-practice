class Solution:
    def reverseString(self, s) -> None:
        firstPointer = 0
        secondPointer = len(s) - 1

        while firstPointer < secondPointer:
            s[firstPointer], s[secondPointer] = s[secondPointer], s[firstPointer]
            firstPointer += 1
            secondPointer -= 1
        

s = ["h","e","l","l","o"]
solution = Solution()
result = solution.reverseString(s)
print(result)


        