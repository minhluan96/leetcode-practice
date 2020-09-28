import heapq

class Solution:
    def qheap1(self, Q, lines):

        q = []

        for i in range(Q):
            line = lines[i]
            firstEl = line[0]

            if firstEl == 1:
                secondEl = line[1]
                heapq.heappush(q, secondEl)
            elif firstEl == 2:
                secondEl = line[1]
                q.remove(secondEl)
                heapq.heapify(q)
            else:
                print(q[0])


if __name__ == '__main__':
    Q = int(input())

    lines = []
    for _ in range(Q):
        lines.append(list(map(int, input().split())))

    solution = Solution()
    solution.qheap1(Q, lines)

