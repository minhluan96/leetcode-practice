import heapq

if __name__ == '__main__':
    N = int(input())
    counter = 0
    '''
    min heap chứa những giá trị lớn nhất
    max heap chứ những giá trị nhỏ nhất
    '''
    min_h = []
    max_h = []

    for _ in range(N):
        lines = list(map(int, input().split()))
        if lines[0] == 1:
            counter += 1
            score = lines[1]

            '''
            Đây là phần nửa đầu, những review sẽ hiện
            Cần phải chuyển những giá trị lớn nhất qua min heap, và giá trị nhỏ nhất qua max heap
            '''
            if counter % 3 == 0:
                if score > -max_h[0]:
                    heapq.heappush(min_h, score)
                else:
                    heapq.heappush(min_h, -heapq.heappop(max_h))
                    heapq.heappush(max_h, -score)
            else:
                '''
                Đây là nửa sau, các giá trị nhỏ nhất sẽ đc đưa vào max heap nếu min heap rỗng.
                Nếu minn heap không rỗng thì chuyển đổi các giá trị lớn nhất sang min heap
                '''
                if len(min_h) and score > min_h[0]:
                    heapq.heappush(max_h, -heapq.heappop(min_h))
                    heapq.heappush(min_h, score)
                else:
                    heapq.heappush(max_h, -score)
        else:
            if len(min_h) > 0:
                print(min_h[0])
            else:
                print('No reviews yet')


