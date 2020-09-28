class Solution:
    def big_segment(self, n, segments):
        if n == 0: return -1

        maximum = max(segments[0])
        minimum = min(segments[0])

        for i in range(1, len(segments)):
            min_value = min(segments[i])
            max_value = max(segments[i])

            maximum = max(maximum, max_value)
            minimum = min(minimum, min_value)
        
        
        index = -1

        for i in range(len(segments)):
            if segments[i] == [minimum, maximum]:
                index = i + 1

        return index
        
            

n = 6
segments = [
    [3, 3],
    [4, 4],
    [5, 5],
]

# segments = [
#     [1, 5],
#     [2, 3],
#     [1, 10],
#     [7, 10],
#     [7, 7],
#     [10, 10],
# ]

# segments = [
#     [4, 8],
#     [5, 5],
#     [3, 10],
#     [5, 8],
# ]

# segments = [
#     [4, 9],
#     [6, 10],
#     [3, 10],
#     [2, 5],
#     [4, 8],
#     [4, 4],
#     [9, 10],
#     [7, 11]
# ]

# n = int(input())
# segments = []
# for i in range(n):
#     segment = list(map(int, input().split()))
#     segments.append(segment)

solution = Solution()
result = solution.big_segment(n, segments)
print(result)
            
            