class Solution:
    map_c = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        

    def romanToInt(self, s: str) -> int:
        i = 0
        result = 0

        while i < len(s):
            s1 = self.map_c[s[i]]

            if i + 1 < len(s):
                s2 = self.map_c[s[i + 1]]
                
                if s1 >= s2:
                    result += s1
                    i += 1
                else:
                    result += s2 - s1
                    i += 2
            else:
                result += s1
                i += 1
        
        return result


#tc = "MMCCCXCIX"
tc = "MMCDXXV"
solution = Solution()
result = solution.romanToInt(tc)
print(result)