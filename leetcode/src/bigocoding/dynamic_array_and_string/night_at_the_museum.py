class Solution:
    def night_at_museum(self, string):
        minimum = 0
        ALL_CHARACTERS = 26
        HALF_OF_CLOCK = 13
        current = 'a'
        for s in string:
            sub = abs(ord(current) - ord(s))
            if sub < HALF_OF_CLOCK:
                minimum += sub
            else:
                minimum += ALL_CHARACTERS - sub
            current = s
        return minimum

tc = input()
solution = Solution()
result = solution.night_at_museum(tc)
print(result)