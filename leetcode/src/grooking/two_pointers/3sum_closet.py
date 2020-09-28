class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        diff = float('inf')
        nums.sort()

        for i in range(len(nums) - 2):
            firstPointer = i + 1
            lastPointer = len(nums) - 1

            while firstPointer < lastPointer:                
                total = nums[i] + nums[firstPointer] + nums[lastPointer]
                
                if abs(target - total) < abs(diff):
                    diff = target - total

                if total < target:
                    firstPointer += 1
                else:
                    lastPointer -= 1
            
        return target - diff 

nums = [1,1,-1,-1,3]
target = -1

nums = [1,1,1,0]
target = -100

nums = [1,1,-1]
target = 2

nums = [0,2,1,-3]
target = 1

solution = Solution()
result = solution.threeSumClosest(nums, target)
print(result)

