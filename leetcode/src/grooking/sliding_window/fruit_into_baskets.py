'''
Time complexity O(N), the outer loop only executed each element once is O(N), the inner while also process each element once
Therefore the total time complexity is O(N + N) = O(N)

Space complexity is O(K)
'''
class Solution:
    def fruit_into_basket(self, tree, baskets = 2):
        windowStart = 0
        treeTypeFrequency = {}
        maxFruitsCarry = 0

        for windowEnd in range(len(tree)):
            rightTree = tree[windowEnd]

            if rightTree not in treeTypeFrequency:
                treeTypeFrequency[rightTree] = 0
            treeTypeFrequency[rightTree] += 1

            while len(treeTypeFrequency) > baskets:
                leftTree = tree[windowStart]

                treeTypeFrequency[leftTree] -= 1
                if treeTypeFrequency[leftTree] == 0:
                    del treeTypeFrequency[leftTree]
                windowStart += 1

            maxFruitsCarry = max(maxFruitsCarry, windowEnd - windowStart + 1)
        
        return maxFruitsCarry

tree = []
solution = Solution()
result = solution.fruit_into_basket(tree)
print(result)