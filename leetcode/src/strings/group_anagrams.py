class Solution:
    def groupAnagrams(self, strs):
        sorted_strs = list(map(lambda s: ''.join(sorted(s)), strs))

        counter = 0
        pos_map = {}
        
        while counter < len(sorted_strs):
            if sorted_strs[counter] in pos_map:
                pos_map[sorted_strs[counter]].append(strs[counter])
            else:
                pos_map[sorted_strs[counter]] = [strs[counter]]

            counter += 1
        
        return list(pos_map.values())

s = ["eat", "tea", "tan", "ate", "nat", "bat"]

'''This solution will have O(N) time complexity since we have to loop through all the list to sort and to categorize'''
'''Space complexity is O(N)'''

solution = Solution()
# result = solution.groupAnagrams(s)
# print(result)

import collections

class Solution2:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

s = ["eat", "tea", "tan", "ate", "nat", "bat"]

solution = Solution2()
result = solution.groupAnagrams(s)
print(result)

'''
Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs.
The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.

Space Complexity: O(NK), the total information content stored in ans.
'''