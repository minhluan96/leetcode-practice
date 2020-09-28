class Solution:
    def expand_around_center(self, s, left, right):
        L = left
        R = right
        counter = 0

        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
            counter += 1

        return counter


    def countSubstrings(self, s: str) -> int:
        if not s: return ''

        counter = 0

        for i in range(len(s)):
            count_len1 = self.expand_around_center(s, i, i)
            count_len2 = self.expand_around_center(s, i, i + 1)
            
            if count_len1 > 0:
                counter += count_len1
            if count_len2 > 0:
                counter += count_len2
        
        return counter

s = "aaaaa"
solution = Solution()
result = solution.countSubstrings(s)
print(result)