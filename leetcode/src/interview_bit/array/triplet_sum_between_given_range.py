class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        nums = list(map(float, A))
        nums.sort()

        for i in range(len(A) - 2):
            j = i + 1
            k = j + 1

            a = nums[i] + nums[j] + nums[k]
            '''
            If a > 2 which mean the value is out of range so we need to combine the 2 smallest values.
            If the result still > 2 which mean no matter the combination, it always greater than 2
            Otherwise, it satisfied the requirement.
            '''
            if a > 2:
                a = nums[k] + nums[0] + nums[1]

            if 1 < a < 2:
                return 1

        return 0


if __name__ == '__main__':
    A = [ "0.234022", "0.051717", "0.820402", "0.492629", "0.004825", "0.589073" ]
    solution = Solution()
    result = solution.solve(A)
    print(result)