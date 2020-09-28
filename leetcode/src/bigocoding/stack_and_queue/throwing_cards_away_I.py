import queue

class Solution:
    def throwinngCardsAwayI(self, n):
        cards = queue.Queue()
        discards = []

        for i in range(n):
            cards.put(i + 1)

        while cards.qsize() > 1:
            top = cards.get()
            second = cards.get()
            discards.append(top)
            cards.put(second)

        return [list(cards.queue), discards]


while True:
    n = int(input())
    if n == 0:
        break

    solution = Solution()
    result = solution.throwinngCardsAwayI(n)
    cards = [str(integer) for integer in result[0]]
    discards = [str(integer) for integer in result[1]]
    if not len(result[1]):
        print('Discarded cards:')
    else:
        print('Discarded cards: {}'.format(', '.join(discards)))
    
    if not len(result[0]):
        print('Remaining cards:')
    else:
        print('Remaining card: {}'.format(', '.join(cards)))

        