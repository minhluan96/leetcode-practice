class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        result = []
        i = len(A) - 1
        remember = 0
        while i >= 0:
            new_number = A[i] + 1 + remember
            if new_number > 9:
                result.append(0)
            else:
                result.append(new_number)
                break

            i -= 1

        result = result[::-1]
        if i >= 0:
            result = A[:i] + result
        else:
            if result[0] == 0:
                result = [1] + result

        for j in range(len(result)):
            if result[j] != 0:
                break

        result = result[j:]

        return result


if __name__ == '__main__':
    A = [ 0, 0, 4, 4, 6, 0, 9, 6, 5, 1 ]
    solution = Solution()
    result = solution.plusOne(A)
    print(result)

