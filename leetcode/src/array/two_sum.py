class Solution:
    '''
        Using brute force O(n)
    '''
    def twoSum(self, nums, target):
        counter = 0
        for i in range(len(nums) - 1):
            substract = target - nums[i]
            
            substr_arr = nums[i + 1:]
            counter += 1

            if substract in substr_arr:
                other_pair = substr_arr.index(substract) + counter
                return [i, other_pair]
        
        return []


class Solution2:
    '''
        Using two-pass hash table (dict) O(n) - space complexity O(n)
    '''
    def twoSum(self, nums, target):
        nmap = {}
        for i in range(len(nums)):
            nmap[nums[i]] = i

        for i in range(len(nums) - 1):
            substract = target - nums[i]

            if substract in nmap.keys() and nmap[substract] != i:
                return [i, nmap[substract]]

        
        return []


class Solution3:
    '''
        Using one-pass hash table (dict) O(n) - space complexity O(1)
    '''
    def twoSum(self, nums, target):
        nmap = {}
        for i in range(len(nums)):
            substract = target - nums[i]

            if substract in nmap.keys():
                return [nmap[substract], i]

            nmap[nums[i]] = i
        
        return []




nums = [3, 3]
target = 6
solution = Solution3()
result = solution.twoSum(nums, target)
print(result)
        