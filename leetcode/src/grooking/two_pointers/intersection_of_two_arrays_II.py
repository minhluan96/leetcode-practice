class Solution:
    def intersect(self, nums1, nums2):
        firstPointer = 0
        secondPointer = 0
        result = []

        nums1.sort()
        nums2.sort()

        while firstPointer < len(nums1) and secondPointer < len(nums2):
            if nums1[firstPointer] < nums2[secondPointer]:
                firstPointer += 1
            elif nums1[firstPointer] > nums2[secondPointer]:
                secondPointer += 1
            else:
                result.append(nums1[firstPointer])
                firstPointer += 1
                secondPointer += 1

        
        return result

nums1 = [2,1]
nums2 = [1,1]
solution = Solution()
result = solution.intersect(nums1, nums2)
print(result)
