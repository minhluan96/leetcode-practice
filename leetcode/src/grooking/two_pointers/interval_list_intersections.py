class Solution:
    def intervalIntersection(self, A, B):
        pointerA = 0
        pointerB = 0

        results = []

        while pointerA < len(A) and pointerB < len(B):
            pairA = A[pointerA]
            pairB = B[pointerB]

            firstItem, secondItem = 0, 0

            if pairA[1] < pairB[0]:
                pointerA += 1
                continue

            if pairB[1] < pairA[0]:
                pointerB += 1
                continue

            if pairA[0] < pairB[0]:
                firstItem = pairB[0]
            else:
                firstItem = pairA[0]

            if pairA[1] < pairB[1]:
                secondItem = pairA[1]
            else:
                secondItem = pairB[1]

            if pairA[1] < pairB[1]:
                pointerA += 1
            else:
                pointerB += 1

            results.append([firstItem, secondItem])

        
        return results
            

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
solution = Solution()
result = solution.intervalIntersection(A, B)
print(result)