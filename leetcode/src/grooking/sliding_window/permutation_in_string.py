class Solution:
    def permutation_in_string(self, s1, s2):
        characterFrequency = {}

        for i in range(len(s1)):
            if s1[i] not in characterFrequency:
                characterFrequency[s1[i]] = 0
            characterFrequency[s1[i]] += 1

        windowStart = 0
        counter = len(characterFrequency)

        for windowEnd in range(len(s2)):
            rightChar = s2[windowEnd]
            
            if rightChar in characterFrequency:
                characterFrequency[rightChar] -= 1
                if characterFrequency[rightChar] == 0:
                    counter -= 1
            
            while counter == 0:
                leftChar = s2[windowStart]

                if windowEnd - windowStart == len(s1) - 1:
                    return True

                if leftChar in characterFrequency:
                    characterFrequency[leftChar] += 1
                    if characterFrequency[leftChar] > 0:
                        counter += 1
                
                windowStart += 1
        
        return False

s1 = 'ab'
s2 = 'eidboaoo'
solution = Solution()
result = solution.permutation_in_string(s1, s2)
print(result)