class Solution:
    def intervalIntersection(self, A, B):
        start, end = 0, 1
        i, j = 0, 0
        results = []

        while i < len(A) and j < len(B):
            a_overlaps_b = A[i][start] <= B[j][end] and A[i][end] >= B[j][end]

            b_overlaps_a = B[j][start] <= A[i][end] and B[j][end] >= A[i][end]

            if a_overlaps_b or b_overlaps_a:
                results.append([max(A[i][start], B[j][start]), min(A[i][end], B[j][end])])

            if A[i][end] < B[j][end]:
                i += 1
            else:
                j += 1

        return results

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
solution = Solution()
result = solution.intervalIntersection(A, B)
print(result) 