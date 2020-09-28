class Solution:
    def productExceptSelf(self, nums):
        '''
            Brute force O(n^2)
        '''
        output = []
        counter = 0
        while len(output) < len(nums):
            for i in range(len(nums)):
                if counter == i: continue
                if len(output) == counter:
                    output.append(nums[i])
                else:
                    output[counter] *= nums[i]
            counter += 1

        return output
        

# tc = [1,2,3,4]
# solution = Solution()
# result = solution.productExceptSelf(tc)
# print(result)




class Solution2:
    '''
    Take O(n) complexity but use 3 * O(n) space
    '''
    def productExceptSelf(self, nums):
        length = len(nums)

        left, right, output = [0] * length, [0] * length, [0] * length

        left[0] = 1
        ''' left[i - 1] already contained all the multiply of the numbers before '''
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        right[length - 1] = 1
        for i in reversed(range(length - 1)):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(length):
            output[i] = left[i] * right[i]

        return output



class Solution3:
    def productExceptSelf(self, nums):
        
        length = len(nums)

        output = [0] * length

        output[0] = 1

        for i in range(1, length):
            output[i] = output[i - 1] * nums[i - 1]
        
        right = 1

        for i in reversed(range(length)):
            '''
            For the index 'i', right would contain the 
            product of all elements to the right. We update R accordingly
            '''
            output[i] = output[i] * right
            right *= nums[i]

        return output



tc = [1, 2, 3, 4]
solution = Solution3()
result = solution.productExceptSelf(tc)
print(result)
