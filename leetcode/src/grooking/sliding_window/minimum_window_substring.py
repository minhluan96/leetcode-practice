class Solution:
    def minimum_window_substring(self, s, t):
        windowStart = 0
        characterFrequency = {}
        minLength = 0
        minSubString = ''        

        for i in range(len(t)):
            if t[i] not in characterFrequency:
                characterFrequency[t[i]] = 0
            characterFrequency[t[i]] += 1

        counter = len(characterFrequency)

        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]

            if rightChar in characterFrequency:
                characterFrequency[rightChar] -= 1
                if characterFrequency[rightChar] == 0:
                    counter -= 1

            while counter == 0:
                leftChar = s[windowStart]

                if leftChar in characterFrequency:
                    characterFrequency[leftChar] += 1
                    if characterFrequency[leftChar] > 0:
                        counter += 1
                
                if minLength == 0 or (windowEnd - windowStart + 1) < minLength:
                    minLength = windowEnd - windowStart + 1
                    minSubString = s[windowStart:windowEnd + 1]

                windowStart += 1
        
        return minSubString

s = "ADOBECODEBANC" 
t = "ABC"
solution = Solution()
result = solution.minimum_window_substring(s, t)
print(result)