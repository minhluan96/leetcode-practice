class Solution:
    def longest_substring(self, s):
        hmap = {}
        counter, begin, end, length_substr = 0, 0, 0, 0

        while end < len(s):
            if s[end] in hmap:
                hmap[s[end]] += 1
                if hmap[s[end]] > 1:
                    counter += 1

            else:
                hmap[s[end]] = 1

            while counter > 0:

                if s[begin] in hmap:
                    if hmap[s[begin]] > 1: # at least has one character in the string
                        counter -= 1
                    hmap[s[begin]] -= 1
                begin += 1

            end += 1
            length_substr = max(length_substr, end - begin)
        
        
        return length_substr



s = 'abcabcbb'
solution = Solution()
result = solution.longest_substring(s)
print(result)