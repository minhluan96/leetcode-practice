import queue
import heapq

if __name__ == '__main__':
    while True:
        try:
            N = int(input())

            is_stack, is_queue, is_priority_queue = True, True, True

            stack = []
            q = queue.Queue()
            pq = []

            for _ in range(N):
                lines = list(map(int, input().split()))

                value = lines[1]
                if lines[0] == 1:
                    if is_stack:
                        stack.append(value)

                    if is_queue:
                        q.put(value)

                    if is_priority_queue:
                        heapq.heappush(pq, -value)
                else:
                    if is_stack:
                        if not len(stack) or stack[-1] != value:
                            is_stack = False
                        else:
                            stack.pop()

                    if is_queue:
                        if q.empty() or q.queue[0] != value:
                            is_queue = False
                        else:
                            q.get()

                    if is_priority_queue:
                        if not len(pq) or -pq[0] != value:
                            is_priority_queue = False
                        else:
                            heapq.heappop(pq)

            if is_stack and not is_queue and not is_priority_queue:
                print('stack')
            elif not is_stack and is_queue and not is_priority_queue:
                print('queue')
            elif not is_stack and not is_queue and is_priority_queue:
                print('priority queue')
            elif not is_stack and not is_queue and not is_priority_queue:
                print('impossible')
            else:
                print('not sure')

        except EOFError:
            break



