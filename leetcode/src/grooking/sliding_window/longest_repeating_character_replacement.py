class Solution:
    def longest_repeating_character_replacement(self, s, k):
        windowStart = 0
        maxLength = 0
        characterFrequency = {}
        maxRepeatingCharacterLength = 0

        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]

            if rightChar not in characterFrequency:
                characterFrequency[rightChar] = 0
            characterFrequency[rightChar] += 1

            maxRepeatingCharacterLength = max(maxRepeatingCharacterLength, characterFrequency[rightChar])

            while (windowEnd - windowStart + 1) - maxRepeatingCharacterLength > k:
                leftChar = s[windowStart]
                characterFrequency[leftChar] -= 1
                if characterFrequency[leftChar] == 0:
                    del characterFrequency[leftChar]
                windowStart += 1
            
            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength

s = 'ABAB'
k = 2
solution = Solution()
result = solution.longest_repeating_character_replacement(s, k)
print(result)