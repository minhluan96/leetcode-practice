class Solution:
    def dressEmInVests(self, n, m, x, y, desires, sizes):
        i, j = 0, 0
        results = []

        while i < n and j < m:
            if ((desires[i] - x <= sizes[j]) and (desires[i] + y >= sizes[j])) or \
                (desires[i] == sizes[j]):
                results.append([i + 1, j + 1])
                i += 1
                j += 1
            else:
                '''
                If the desire size bigger than the vest size which mean the current size isn't match we have to
                increase the size
                '''
                if desires[i] - x > sizes[j]:
                    j += 1
                else:
                    '''
                    If the size was larger than the current size, which mean no matter how he try, he still not fit,
                    the best choice is move on to the next solider
                    '''
                    i += 1

        return results


n = 5
m = 3 
x = 0 
y = 0
desires = [1,2,3,3,4]
sizes = [1,3,5]

n = 3
m = 3 
x = 2 
y = 2
desires = [1,5,9]
sizes = [3,5,7]

n = 20
m = 30
x = 2
y = 5
desires = [2,2 ,2 ,2 ,3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6]
sizes = [2 ,2 ,2 ,2 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,4 ,4 ,4 ,4 ,4 ,4 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,6]

n = 2
m = 3
x = 2
y = 5
desires = [2,6]
sizes = [2,3,3]

# firstLine = list(map(int, input().split()))

# n = firstLine[0]
# m = firstLine[1]
# x = firstLine[2]
# y = firstLine[3]
# desires = list(map(int, input().split()))
# sizes = list(map(int, input().split()))

solution = Solution()
result = solution.dressEmInVests(n, m, x, y, desires, sizes)
print(len(result))
for pair in result:
    print('{} {}'.format(pair[0], pair[1]))