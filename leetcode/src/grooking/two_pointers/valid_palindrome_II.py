class Solution:
    def verify(self, s, left, right, deleted):
        while left < right:
            if s[left] != s[right]:
                if deleted:
                    return False
                else:
                    return self.verify(s, left + 1, right, True) or self.verify(s, left, right - 1, True)
            else:
                left += 1
                right -= 1
        
        return True


    def validPalindrome(self, s: str) -> bool:
        return self.verify(s, 0, len(s) - 1, False)

s = 'abc'
solution = Solution()
result = solution.validPalindrome(s)
print(result)