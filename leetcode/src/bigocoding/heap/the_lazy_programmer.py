import heapq

if __name__ == '__main__':
    '''
    Tách nhỏ bài toán
    giả sử các deadline bằng nhau: d1 = d2 = d3 = ... dn = x
    Do các deadline như nhau nên sẽ thực hiện tuần tự từ b1 > b2 > b3 > (x) | ... bN
    
    Nếu x nằm trước b(n), x là deadline thì cần phải tìm thằng có thời gian dài nhất để trả extra, giúp b(n) ko bị lố
    a(i) là số tiền cần trả cho 1h làm
    ~> trả cho max(ai), max(a i+1)
    
    
    Độ phức tạp O(N logN + N logN) = O(2 N logN) ~ O(N logN)
    
    Do mỗi contract đc đưa đúng 1 lần và đc đưa ngay sau đó
    '''

    class Contract:
        def __init__(self, a, b, d):
            self.a = a
            self.b = b
            self.d = d

        def __lt__(self, other):
            return self.d < other.d



    T = int(input())

    while T > 0:
        T -= 1

        N = int(input())

        maps = []
        pq = []
        total = 0
        ans = 0

        for _ in range(N):
            lines = list(map(int, input()))
            c = Contract(lines[0], lines[1], lines[2])
            maps.append(c)

        maps.sort()

        for con in maps:
            total += con.b
            if total > con.d:
                over = total - con.d  # luu phan thua

                while len(pq) and over > 0:
                    c = heapq.heappop(pq)
                    if c.b >= over:
                        over -= c.b
                        c.b -= over
                        ans += over / c.a
                    else:
                        over -= c.b
                        c.b = 0
                        ans += c.b / c.a

                    if c.b > 0:
                        heapq.heappush(pq, c)

        print(ans)








