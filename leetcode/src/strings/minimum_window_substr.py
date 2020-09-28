class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        1. Use two pointers: start and end to represent a window.
        2. Move end to find a valid window.
        3. When a valid window is found, move start to find a smaller window.
        
        To check if a window is valid, we use a map to store (char, count) for chars in t.
        And use counter for the number of chars of t to be found in s. The key part is m[s[end]]--;.
        We decrease count for each char in s. If it does not exist in t, the count will be negative.  
        '''
        hmap = {}

        counter, start, end, min_len = len(t), 0, 0, -1

        min_start = 0

        ''' First, we register the number apperances of every character in T to the hashmap '''

        for c in t:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 1

        while end < len(s):
            '''
            If the character existed in the string S, we decreased counter. Otherwise, we will put the
            character in the hashmap with the default value is 0 because it's never existed in the T string
            '''
            if s[end] in hmap:
                if hmap[s[end]] > 0:
                    counter -= 1
            else:
                hmap[s[end]] = 0
            
            '''
            Always decreased the value of the character in the hashmap. 
            If the character not existed in T, the value will be negative
            '''
            hmap[s[end]] -= 1

            while counter == 0:
                if end - start < min_len or min_len == -1:
                    ''' The actual length will be the result of addition of the subtraction end position and start position with one '''
                    min_len = end - start + 1
                    min_start = start
                
                ''' 
                Always increased the value of the character at start position in s
                Because for characters that do not exist in T, hmap[s[start]] never be > 0. 
                Because it already went through -- earlier during hmap[s[end]] -= 1

                assume T = "abc"
                ddddddabcdabc
                ^-------^
                start ---- end

                we are now in the inner while loop, the counter is 0 and now we want to minimize the window
                hmap['d'] would actually be -6 because of the -- earlier.
                So hmap[s[start]]+= 1; and if (hmap[s[start]] > 0) used in conjuction will help us skip all the 'd's until we reach 'a',
                and only 'a' is possible to be > 0 when you hmap[s[start]]+= 1 it.
                now counter == 1 and we resume the outer loop.
                '''
                hmap[s[start]] += 1

                if hmap[s[start]] > 0:
                    counter += 1
                
                start += 1

            end += 1

        
        if min_len != -1:
            return s[min_start: min_start + min_len]
        
        return ''


s = 'ADOBECODEBANC'
t = 'ABC'
solution = Solution()
# result = solution.minWindow(s, t)
# print(result)


'''
Using the counter++ instead of counter--
'''

class Solution2:
    def minWindow(self, s: str, t: str) -> str:

        hmap = {}
        counter, start, end, min_start, min_length = 0, 0, 0, 0, -1

        for c in t:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 1
        
        while end < len(s):
            if s[end] in hmap:
                if hmap[s[end]] > 0:
                    counter += 1
            else:
                hmap[s[end]] = 0

            hmap[s[end]] -= 1


            while counter >= len(t):
                if end - start + 1 < min_length or min_length == -1:
                    min_start = start
                    min_length = end - start + 1
                
                hmap[s[start]] += 1

                if hmap[s[start]] > 0:
                    counter -= 1

                start += 1
            
            end += 1

        if min_length != -1:
            return s[min_start : min_start + min_length]

        return ''

s = 'ADOBECODEBANC'
t = 'ABC'
solution = Solution2()
result = solution.minWindow(s, t)
print(result)
