class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not len(needle): return 0

        result = self.search_kmp(haystack, needle)
        if not len(result): return -1
        return result[0]

    def partial(self, pattern):
        """Build a NEXT table"""
        """Calculate partial match table: String -> [Int]"""
        res = [0]

        for i in range(1, len(pattern)):
            j = res[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = res[j - 1]
            res.append(j + 1 if pattern[j] == pattern[i] else j)
        
        return res


    def search_kmp(self, string, pattern):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, res, j = self.partial(pattern), [], 0

        for i in range(len(string)):
            while j > 0 and string[i] != pattern[j]:
                j = partial[j - 1]
            if string[i] == pattern[j]: 
                j += 1
            if j == len(pattern):
                res.append(i - (j - 1))
                j = partial[j - 1]

        return res


string = "Hello"
pattern = "llo"

solution = Solution()
result = solution.search_kmp(string, pattern)

print(result)