class Solution:
    def intersection(self, nums1, nums2):
        '''
            Brute force O(n)
        '''
        result = set()
        for n in nums1:
            if n in nums2:
                result.add(n)
        
        return list(result)

class Solution2:
    def intersection(self, nums1, nums2):
        '''
            Using the counter O(n + m)
        '''
        import collections

        a, b = collections.Counter(nums1), collections.Counter(nums2)

        return list((a & b).elements())



a = [1,2,2,1]
b = [2,2]
solution = Solution()
result = solution.intersection(a, b)
print(result)