class Solution:
    def arrays(self, nA, nB, k, m, a_arr, b_arr):
        if nA < k or nB < m:
            return False
        
        sub_a = a_arr[:k]
        sub_b = b_arr[-m:]

        if sub_a[-1] >= sub_b[0]:
            return False

        return True
        

# first_line = list(map(int, input().split()))
# nA = first_line[0]
# nB = first_line[1]

# second_line = list(map(int, input().split()))
# k = second_line[0]
# m = second_line[1]
# a_arr = list(map(int, input().split()))
# b_arr = list(map(int, input().split()))

nA = 10
nB = 14
k = 10
m = 1
a_arr = [4, 4, 8, 20, 25, 32, 35, 39, 42, 51]
b_arr = [12, 13, 23, 26, 29, 29, 35, 35, 36, 42, 46, 48, 50, 52]

solution = Solution()
result = solution.arrays(nA, nB, k, m, a_arr, b_arr)
if result:
    print('YES')
else:
    print('NO')