'''
Time complexity O(N)
Space complexity O(N)
'''
class Solution:
    def find_all_anagrams_in_a_string(self, s, p):
        characterFrequency = {}

        for i in range(len(p)):
            if p[i] not in characterFrequency:
                characterFrequency[p[i]] = 0
            characterFrequency[p[i]] += 1

        windowStart = 0
        foundIndex = []
        counter = len(characterFrequency)
        
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]

            if rightChar in characterFrequency:
                characterFrequency[rightChar] -= 1
                if characterFrequency[rightChar] == 0:
                    counter -= 1
            
            while counter == 0:
                leftChar = s[windowStart]

                if windowEnd - windowStart == len(p) - 1:
                    foundIndex.append(windowStart)

                if leftChar in characterFrequency:
                    characterFrequency[leftChar] += 1
                    if characterFrequency[leftChar] > 0:
                        counter += 1

                windowStart += 1
        
        return foundIndex

s = 'abab'
p = 'ab'
solution = Solution()
result = solution.find_all_anagrams_in_a_string(s, p)
print(result)