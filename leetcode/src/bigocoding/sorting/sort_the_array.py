class Solution:
    '''
    Time complexity O(NlogN)
    Space complexity O(N)
    '''


    def sortTheArray(self, n, nums):
        sortedNums = sorted(nums)
 
        if sortedNums == nums:
            return [1, 1]
 
        
        leftPos = 0
        rightPos = n - 1
 
        while leftPos < n - 1:
            if nums[leftPos] < nums[leftPos + 1]:
                leftPos += 1
            else:
                break
 
        while rightPos > 1:
            if nums[rightPos] > nums[rightPos - 1]:
                rightPos -= 1
            else:
                break
        
        
        newReverse = nums[:leftPos] + nums[leftPos:rightPos + 1][::-1] + nums[rightPos + 1:]

        if sortedNums == newReverse:
            return [leftPos + 1, rightPos + 1]
        
        return -1
            
            

            
                

# n = 3
# nums = [3,2,1]
# [1,2,3]

# n = 4
# nums = [2,1,3,4]
# # [1,2,3,4]

# n = 4
# nums = [3,1,2,4]
# # [1,2,3,4]

# n = 2
# nums = [1,2]

# n = 6
# nums = [1,3,4,2,5,6]

# n = 8
# nums = [1,2,3,9,8,7,6,5]

# n = 40
# nums = [42131757, 49645896, 49957344, 78716964, 120937785, 129116222, 172128600, 211446903, 247833196, 779340466, 717548386, 709969818, 696716905, 636153997, 635635467, 614115746, 609201167, 533608141, 521874836, 273044950, 291514539, 394083281, 399369419, 448830087, 485128983, 487192341, 488673105, 497678164, 501864738, 265305156, 799595875, 831638598, 835155840, 845617770, 847736630, 851436542, 879757553, 885618675, 964068808, 969215471]

n = int(input())
nums = list(map(int, input().split()))

solution = Solution()
result = solution.sortTheArray(n, nums)
if result != -1:
    print('yes')
    print('{} {}'.format(result[0], result[1]))
else:
    print('no')