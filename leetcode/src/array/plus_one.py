class Solution:
    def plusOne(self, digits):
        ''' Time complexity O(n), space complexity O(1) '''
        remember = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
                remember = 1
            else:
                remember = 0
                break
        
        if remember:
            digits.insert(0, remember)

        return digits

class Solution2:
    def plusOne(self, digits):
        ''' 
            convert to the integer and add 1 and convert back to the list
        '''

        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits) - 1 - i)

        num += 1
        return [int(i) for i in str(num)] 


# tcs:
# - 1 item: [2] ~> [3], [9] ~> [1, 0]
# - 2 items: [2, 3] ~> [2, 4], [2, 9] ~> [3, 0]
# - n items: [a, b] ~> [a, b + 1], [a, 9] ~> [a + 1, 0]  

tc = [4,3,2,1]
solution = Solution2()
result = solution.plusOne(tc)
print(result)