import heapq

class Topic:
    def __init__(self, id, zScore):
        self.id = id
        self.zScore = zScore
        self.newScore = 0

    def increase_zscore(self, type, quantity):
        if type == 1:
            self.newScore += quantity * 50
        elif type == 2:
            self.newScore += quantity * 5
        elif type == 3:
            self.newScore += quantity * 10
        else:
            self.newScore += quantity * 20

    def change_score(self):
        return self.newScore - self.zScore

    def __lt__(self, other):
        if self.change_score() > other.change_score():
            return True
        elif self.change_score() < other.change_score():
            return False
        else:
            return self.id > other.id


class Solution:
    def roy_and_trending_topic(self, N, maps):
        arr = []

        for t in maps:
            heapq.heappush(arr, t)

        result = []
        for _ in range(topTopic):
            top = heapq.heappop(arr)
            result.append(top)

        return result


if __name__ == '__main__':
    N = int(input())

    maps = []

    topTopic = 5

    for _ in range(N):
        id, z, p, l, c, s = list(map(int, input().split()))
        topic = Topic(id, z)
        if p != 0:
            topic.increase_zscore(1, p)
        if l != 0:
            topic.increase_zscore(2, l)
        if c != 0:
            topic.increase_zscore(3, c)
        if s != 0:
            topic.increase_zscore(4, s)

        maps.append(topic)

    solution = Solution()
    result = solution.roy_and_trending_topic(N, maps)

    for t in result:
        print('{} {}'.format(t.id, t.newScore))