import re

class Solution:
    ''' Using regex to format string '''
    def isPalindrome(self, s: str) -> bool:
        formatted_str = re.sub('[^A-Za-z0-9]+', '', s)
        formatted_str = formatted_str.lower()

        return formatted_str[::-1] == formatted_str

s = 'race a car'
solution = Solution()
result = solution.isPalindrome(s)
print(result)

class Solution2:
    ''' Using isalnum() '''
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(e for e in s if e.isalnum()).lower()
        return new_s[::-1] == new_s

s = 'race a car'
solution = Solution2()
result = solution.isPalindrome(s)
print(result)

''' In both cases, we use the new array to store the new formated string, therefore, the time complexity is O(n), space complexity is O(n)'''