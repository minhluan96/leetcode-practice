class Solution:

    def expand_around_center(self, s, left, right):
        '''
        Checking the palindrome of a string and return the length of the palindrome string 
        '''
        L = left
        R = right

        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        
        return R - L - 1


    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1: return ''

        start, end = 0, 0
        for i in range(len(s)):
            '''
            Because there are two cases of a palindrome string (abba, racecar). One odd and one even
            And we don't know which case will be fall so we will find the palindrome for both cases
            The len1 is for the odd because in the 'racecar' when we start from the middle is the 'c' character and we will expand to the both sides.
                So the middle character will be the same at the begining. That's why we pass 'i' to the function only

            The len2 is for the even case, because in the 'abba', the middle position can't be exactly what we have done in the odd case.
                Therefore, we will expand it from the begining of the string. The left is equal to 'i' and the right is equal to 'i+1' and expand from it
            '''
            len1 = self.expand_around_center(s, i, i) 
            len2 = self.expand_around_center(s, i, i + 1)
            new_len = max(len1, len2)
            if new_len > end - start:
                '''
                We will have to set the start to the begining of the sub palindrome string, and the end to the end of the palindrome string.
                The i position is the middle position so if we want to jump to the start position, we have to minus half of the len of the palindrome string 
                The same as the end, we will have to add half of the len of the palindrome string
                '''
                start = i - int((new_len - 1) / 2)
                end = i + int(new_len / 2)
        
        return s[start:end + 1]


s = "abb"
solution = Solution()
result = solution.longestPalindrome(s)
print(result)
