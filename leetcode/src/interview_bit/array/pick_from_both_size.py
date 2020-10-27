class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sumP = sum(A[:B])
        sumS = 0

        total = sumP

        i = B - 1
        j = len(A) - 1

        for _ in range(B):
            sumP -= A[i]
            sumS += A[j]

            total = max(total, sumP + sumS)
            i -= 1
            j -= 1

        return total


if __name__ == '__main__':
    A = [-533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35]
    B = 48
    solution = Solution()
    result = solution.solve(A, B)
    print(result)