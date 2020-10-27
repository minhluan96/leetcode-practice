class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        if A < 3:
            return 0

        total = sum(B)

        if total % 3 != 0:
            return 0

        part = total // 3
        cnt = [0] * A
        possible = 0

        temp = 0
        for i in range(A - 1, -1, -1):
            temp += B[i]
            if temp == part:
                cnt[i] = 1

        for i in range(A - 2, -1, -1):
            cnt[i] += cnt[i + 1]

        temp = 0
        for i in range(A - 2):
            temp += B[i]
            if temp == part:
                possible += cnt[i + 2]

        return possible


if __name__ == '__main__':
    '''
    If sum of all the elements of the array is not divisible by 3, return 0.
    It is obvious that the sum of each part of each contiguous part will be equal to the sum of all elements divided by 3.
    Let’s create an array cnt[ ], where cnt[ i ] equals 1, if the sum of elements from ith to Ath equals Array_Sum/3 else 0. Now, calculate the cumulative sum of the cnt array from the last index.
    Thus, we receive very simple solution: for each prefix of initial array 1…i with the sum that equals Array_Sum/3 we need to add to the answer sums[ i+2 ].
    '''
    A = 4
    B = [0, 1, -1, 0]
    solution = Solution()
    result = solution.solve(A, B)
    print(result)