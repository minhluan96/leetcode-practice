'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''

'''
Time complexity O(N). The outer for only run all character only once, the inner while process each character only once. 
Therefore the total algorithm time complexity is O(N + N) = O(N)

Space complexity is O(K)
'''
class Solution:
    def longest_substring_with_k_distinct_characters(self, str1, k):
        windowStart = 0
        maxLength = 0
        characterFrequency = {}

        for windowEnd in range(len(str1)):
            rightChar = str1[windowEnd]

            if rightChar not in characterFrequency:
                characterFrequency[rightChar] = 0
            characterFrequency[rightChar] += 1

            while len(characterFrequency) > k:
                leftChar = str1[windowStart]
                characterFrequency[leftChar] -= 1
                if characterFrequency[leftChar] == 0:
                    del characterFrequency[leftChar]
                windowStart += 1

            maxLength = max(maxLength, windowEnd - windowStart + 1)
        
        return maxLength

            
str1 = 'cbbebi'
k = 3
solution = Solution()
result = solution.longest_substring_with_k_distinct_characters(str1, k)
print(result)