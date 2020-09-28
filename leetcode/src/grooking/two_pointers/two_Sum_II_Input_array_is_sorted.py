class Solution:
    def twoSum(self, numbers, target: int):
        firstPointer = 0
        secondPointer = len(numbers) - 1

        while firstPointer < secondPointer:
            if numbers[firstPointer] + numbers[secondPointer] > target:
                secondPointer -= 1
            
            if numbers[firstPointer] + numbers[secondPointer] < target:
                firstPointer += 1
            
            if numbers[firstPointer] + numbers[secondPointer] == target:
                return [firstPointer + 1, secondPointer + 1]
        
        return []

numbers = [2,7,11,15]
target = 9
solution = Solution()
result = solution.twoSum(numbers, target)
print(result)
        