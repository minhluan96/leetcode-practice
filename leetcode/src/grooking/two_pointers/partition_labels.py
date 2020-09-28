class Solution:
    '''
    Figure out the rightmost index first and use it to denote the start of the next section.
    Reset the left pointer at the start of each new section.
    Store the difference of right and left pointers + 1 as in the result for each section.
    '''
    
    def partitionLabels(self, S: str):
        results = []
        rightMost = {}

        for i, character in enumerate(S):
            rightMost[character] = i

        firstPointer = 0
        secondPointer = 0

        for i, character in enumerate(S):
            secondPointer = max(secondPointer, rightMost[character])

            if i == secondPointer:
                results.append(secondPointer - firstPointer + 1)
                firstPointer = i + 1
        
        return results

S = 'ababcbacadefegdehijhklij'
solution = Solution()
result = solution.partitionLabels(S)
print(result)