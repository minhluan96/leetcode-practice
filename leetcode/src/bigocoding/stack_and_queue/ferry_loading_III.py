import queue

class Car:
    def __init__(self, id, arrivedTime):
        self.id = id
        self.arrivedTime = arrivedTime


class Solution:
    def ferry_loading_III(self, queueLeft, queueRight):
        currentTime = 0
        currentSide = 'left'

        ans = [0 for _ in range(M)]

        while not queueLeft.empty() or not queueRight.empty():
            nextTime = 0

            if not queueLeft.empty() and queueRight.empty():
                nextTime = queueLeft.queue[0].arrivedTime
            elif queueLeft.empty() and not queueRight.empty():
                nextTime = queueRight.queue[0].arrivedTime
            else:
                nextTime = min(queueLeft.queue[0].arrivedTime, queueRight.queue[0].arrivedTime)

            if currentTime < nextTime:
                currentTime = nextTime

            served = 0

            '''Using a variable to determine which queue should be used'''
            executedQueue = queueLeft if currentSide == 'left' else queueRight

            while not executedQueue.empty():
                car = executedQueue.queue[0]
                if car.arrivedTime <= currentTime and served < N:
                    ans[car.id] = currentTime + T
                    served += 1
                    executedQueue.get()
                else:
                    break

            '''
            Assigned back the value to that queue
            '''
            if currentSide == 'left':
                queueLeft = executedQueue
            else:
                queueRight = executedQueue

            '''Change side'''
            currentTime += T
            currentSide = 'right' if currentSide == 'left' else 'left'

        for k in ans:
            print(k)



if __name__ == '__main__':
    C = int(input())

    for g in range(C):
        N, T, M = list(map(int, input().split()))

        cars = []
        queueLeft = queue.Queue()
        queueRight = queue.Queue()

        for i in range(M):
            lines = list(input().split())
            if lines[1] == 'left':
                queueLeft.put(Car(i, int(lines[0])))
            else:
                queueRight.put(Car(i, int(lines[0])))

        solution = Solution()
        solution.ferry_loading_III(queueLeft, queueRight)

        if g != C - 1:
            print()
