# import heapq
#
# if __name__ == '__main__':
#     N = int(input())
#
#     min_h = []
#     max_h = []
#     total = 0
#
#     for _ in range(N):
#         lines = list(map(int, input().split()))
#         if lines[0] > 0:
#             for t in lines[1:]:
#                 if len(min_h):
#                     if t > min_h[0]:
#                         heapq.heappush(max_h, -t)
#                     else:
#                         heapq.heappush(min_h, t)
#                 else:
#                     heapq.heappush(min_h, t)
#
#         total += -max_h[0] - min_h[0]
#         heapq.heappop(max_h)
#         heapq.heappop(min_h)
#
#         '''
#         Missing case that when the max_h is empty, how to push the max value into this from the min heap?
#         '''
#
#     print(total)
#
#     min_h = []
#     max_h = []
#     mapFrequency = {}
#     result = 0
#     counter = 0
#
#     for _ in range(N):
#         lines = list(map(int, input().split()))
#         if lines[0] > 0:
#             for j in lines[1:]:
#                 counter += 1
#
#                 heapq.heappush(min_h, (j, counter))
#                 heapq.heappush(max_h, (j, counter))
#
#                 if counter not in mapFrequency:
#                     mapFrequency[counter] = False
#
#                 while mapFrequency[min_h[0].counter]:
#                     heapq.heappop(min_h)
#
#                 while mapFrequency[max_h[0].counter]:
#                     heapq.heappop(max_h)
#
#                 result += max_h[0].j - min_h[0].j
#                 mapFrequency[max_h[0].counter] = True
#                 mapFrequency[min_h[0].counter] = True
#
#                 heapq.heappop(max_h)
#                 heapq.heappop(min_h)
#
#     print(result)
#
#
#
#

'''
Answer:
We need to mark the ticket using its index to determine whether they have been taken out from the basket or not
'''

import heapq


if __name__ == '__main__':
    N = int(input())

