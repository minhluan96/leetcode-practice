import queue

import queue

class Solution:
    def processingQueries(self, n, b, queries):
        queriesLine = []
        results = []
        processing = queue.Queue()

        for i in range(len(queries)):
            query = queries[i]
            obj = { 'id': i, 'at': query[0], 'duration': query[1] }
            queriesLine.append(obj)

        queriesLine.sort(key=lambda x: x['at'])

        currentTime = queriesLine[0]['at'] + queriesLine[0]['duration']
        results = [0] * n
        results[0] = currentTime
        
        pos = 1

        while True:
            if pos >= n and processing.qsize() == 0:
                break

            while pos < n:
                if queriesLine[pos]['at'] >= currentTime:
                    break
                if processing.qsize() >= b:
                    results[queriesLine[pos]['id']] = -1
                    pos += 1
                else:
                    processing.put(queriesLine[pos])
                    pos += 1
            
            if processing.qsize() == 0:
                currentTime = queriesLine[pos]['at'] + queriesLine[pos]['duration']
                results[pos] = currentTime
                pos += 1
                continue
            
            obj = processing.get()
            currentTime += obj['duration']
            results[obj['id']] = currentTime
                

        return results

# n = 5 
# b = 1
# queries = [
# [2 ,9],
# [4 ,8],
# [10, 9],
# [15, 2],
# [19, 1],
# ]

# n = 4
# b = 1
# queries = [
# [2 ,8],
# [4 ,8],
# [10, 9],
# [15, 2],
# ]

firstLine = list(map(int, input().split()))
n = firstLine[0]
b = firstLine[1]

queries = []
for i in range(n):
    line = list(map(int, input().split()))
    queries.append(line)

solution = Solution()
result = solution.processingQueries(n, b, queries)
print(*result)


        

