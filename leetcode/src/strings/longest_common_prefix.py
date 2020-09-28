class YourSolution:

    def shortestString(self, strs):
        min = len(strs[0])
        shortest_str = strs[0]
        for string in strs:
            if len(string) < min:
                min = len(string)
                shortest_str = string
        return shortest_str

    def longestCommonPrefix(self, strs) -> str:
        """ Complexity: O(n^m) 
            unacceptable
        """
        length_strs = len(strs)
        if not length_strs:
            return ""
        elif length_strs == 1:
            return strs[0]

        shortest_str = self.shortestString(strs)
        strs_without_shortest = strs[:]
        strs_without_shortest.remove(shortest_str)
        prefix = ""

        if not len(shortest_str): 
            return prefix

        for i in range(0, len(shortest_str)):
            found = False

            for string in strs_without_shortest:
                if string[i] == shortest_str[i]:
                    found = True
                else:
                    found = False
                    break

            if found:
                prefix += shortest_str[i]
            else:
                break

        return prefix



"""
    Testcases:
    ["aca", "cba"]
    []
    ["", ""]
    ["a"]
    ["aa", "aa"]
    ["flower","flow","flight"]
"""
input = ['aa', 'aa']
solution = YourSolution()
result = solution.longestCommonPrefix(input)
# print(result)

"""
============================================
"""

class Solution:
    """
        Using tuple, set and zip
    """

    def longestCommonPrefix(self, strs) -> str:
        prefix = ""
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix += x[0]
            else:
                break
        
        return prefix

input = ["flower","flow","flight"]
solution = Solution()
result = solution.longestCommonPrefix(input)
#print(result)

import sys

class BinarySearchSolution:

    def longestCommonPrefix(self, strs) -> str:
        if not len(strs) or strs == None:
            return ""
        min_len = sys.maxsize

        for string in strs:
            min_len = min(min_len, len(string))
        
        low = 1
        high = min_len
        while low < high:
            middle = int((low + high) / 2)
            
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        
        return strs[0][0 : int((low + high) / 2)]
            

    def isCommonPrefix(self, strs, len):
        str1 = strs[0][:len]
        
        for string in strs[1:]:
            if not string.startswith(str1):
                return False
        
        return True

input = ["flower","flow","flight"]
solution = BinarySearchSolution()
result = solution.longestCommonPrefix(input)
print(result)