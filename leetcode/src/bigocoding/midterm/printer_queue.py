import heapq
import queue

class Node:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos

    def __lt__(self, other):
        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.pos > other.pos:
                return True
        return False

class Solution:
    def printer_queue(self):
        timer = 0
        while len(pq):
            node = heapq.heappop(pq)
            if node.pos != m:
                timer += 1
            else:
                break

        return timer + 1

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, m = list(map(int, input().split()))
        nums = list(map(int, input().split()))

        q = queue.Queue()
        pq = []

        for i in range(n):
            q.put((nums[i], i))

        executed = queue.Queue()
        for i in range(n):
            

        solution = Solution()
        result = solution.printer_queue()
        print(result)




