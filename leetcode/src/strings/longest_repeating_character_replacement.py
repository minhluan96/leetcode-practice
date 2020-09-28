class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}

        begin, end, max_substr = 0, 0, 0

        max_c_length = 0

        while end < len(s):
            if s[end] in hmap:
                hmap[s[end]] += 1
            else:
                hmap[s[end]] = 1

            if hmap[s[end]] > max_c_length:
                max_c_length = hmap[s[end]]

            ''' I'm not using the counter here because when assigned the counter = max_c_length
            which mean the max_c_length sometimes is bigger than k which we will cost at least a step to 
            slide the window and make the result return false
            '''
            # if (end - begin + 1) - max_c_length > k:
            #     counter = max_c_length
            # while counter > 0

            while end - begin + 1 - max_c_length > k:
                if s[begin] in hmap:
                    hmap[s[begin]] -= 1
                begin += 1
            
            end += 1
            max_substr = max(max_substr, end - begin)

        return max_substr


s = 'AABA'
k = 0
solution = Solution()
result = solution.characterReplacement(s, k)
print(result)