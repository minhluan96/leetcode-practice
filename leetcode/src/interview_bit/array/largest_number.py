class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return int(self.value + other.value) > int(other.value + self.value)

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        dups = list(A)
        if len(set(dups)) == 1 and dups[0] == 0:
            return 0

        nums = []
        for i in range(len(A)):
            number = Number(str(A[i]))
            nums.append(number)

        nums.sort()
        result = ''
        for i in range(len(nums)):
            result += nums[i].value
        return result

if __name__ == '__main__':
    A = [ 0, 0, 0, 0, 0 ]
    solution = Solution()
    result = solution.largestNumber(A)
    print(result)