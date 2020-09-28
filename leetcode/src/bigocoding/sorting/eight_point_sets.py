class Solution:
    def eightPointSets(self, listPairs):

        listX = list(pair[0] for pair in listPairs)
        listY = list(pair[1] for pair in listPairs)

        setX = sorted(list(set(listX)))
        setY = sorted(list(set(listY)))

        if len(setX) != 3 or len(setY) != 3:
            return -1
        
        '''
        Have to sort the listPairs in order to check
        '''
        listPairs.sort()

        if [setX[1], setY[1]] in listPairs:
            if listPairs.index([setX[1], setY[1]]) == int(len(listPairs) / 2):
                return -1

        listPairFrequency = {}

        for i in range(len(listPairs)):
            tuplePair = tuple(listPairs[i])
            if tuplePair not in listPairFrequency:
                listPairFrequency[tuplePair] = 0
            listPairFrequency[tuplePair] += 1

        if len(listPairFrequency) != len(listPairs):
            return -1

        return 1


# class Answer:
#     def eightPointSets(self, listPairs):


# listPairs = [
# [0,0],
# [0,1],
# [0,2],
# [1,0],
# [1,2],
# [2,0],
# [2,1],
# [2,2],
# ]

# listPairs = [
# [0,0],
# [1,0],
# [2,0],
# [3,0],
# [4,0],
# [5,0],
# [6,0],
# [7,0],
# ]

listPairs = [
[1,1],
[1,2],
[1,3],
[2,1],
[2,2],
[2,3],
[3,1],
[3,2],
]

# listPairs = [
# [0,0],
# [2,1],
# [1,0],
# [0,2],
# [2,2],
# [1,0],
# [2,1],
# [0,2],
# ]

# listPairs = [
# [18907,19018],
# [17787,18949],
# [1391,22785],
# [17787,22785],
# [1391,18949],
# [1391,19018],
# [18907,22785],
# [18907,18949],
# ]

listPairs = [
[578 ,123],
[713 ,216],
[5, 17],
[578 ,216],
[713 ,123],
[5 ,123],
[5 ,216],
[578, 17],
]

# listPairs = []
# for i in range(8):
#     pairs = list(map(int, input().split()))
#     listPairs.append(pairs)


solution = Solution()
result = solution.eightPointSets(listPairs)
if result == 1:
    print('respectable')
else:
    print('ugly')

        


        