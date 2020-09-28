class Solution:
    def isPalindrome(self, s: str) -> bool:
        firstPointer = 0
        lastPointer = len(s) - 1

        while firstPointer < lastPointer:
            leftChar = s[firstPointer].lower()
            rightChar = s[lastPointer].lower()

            if not leftChar.isalpha() and not leftChar.isdigit():
                firstPointer += 1
                continue

            if not rightChar.isalpha() and not rightChar.isdigit():
                lastPointer -= 1
                continue
                
            if leftChar != rightChar:
                return False

            firstPointer += 1
            lastPointer -= 1
        
        return True

s = 'race a car'
solution = Solution()
result = solution.isPalindrome(s)
print(result)

