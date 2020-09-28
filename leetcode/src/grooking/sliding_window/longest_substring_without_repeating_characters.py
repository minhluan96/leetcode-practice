class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        maxLength = 0
        characterFrequency = {}

        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            if rightChar not in characterFrequency:
                characterFrequency[rightChar] = 0
            characterFrequency[rightChar] += 1

            while (windowEnd - windowStart + 1) > len(characterFrequency):
                leftChar = s[windowStart]
                characterFrequency[leftChar] -= 1
                if characterFrequency[leftChar] == 0:
                    del characterFrequency[leftChar]
                
                windowStart += 1
            
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        
        return maxLength

s = 'pwwkew'
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)