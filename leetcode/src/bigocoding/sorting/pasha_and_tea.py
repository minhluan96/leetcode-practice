class Solution:
    def pashaAndTea(self, n, w, cups):
        cups.sort()

        minAmount = float('inf')

        girlAmount = cups[0]
        boyAmount = cups[n] / 2
        averageAmount = w / (3 * n)

        minAmount = min(boyAmount, girlAmount)
        minAmount = min(minAmount, averageAmount)

        return minAmount * 3 * n


class Answer:

    '''
    Example 2:
    gái luôn ít nc hơn trai ~> dành những ly lớn hơn cho trai
    ~> n ly lớn nhất cho trai

    4  4  4  2 2 2
    2x 2x 2x x x x  = w ~> x

    ~> sort mảng ly trà
    a1 <= a2 <= ... <= a(N+1) <= ... <= a(2N)
    x
    ---gái-----       ----trai ----------

    x của gái = ly nhỏ nhất chứa đủ nc ~> min(a1, a((n + 1)/ 2))

    mà total = xn + 2xn = 3x n
    ~> out = min(w, 3xn) do chỉ có w nước
    '''

    def pashaAndTea(self, n, w, cups):
        cups.sort()


        x = min(cups[0], cups[n] / 2)
        return min(w, 3 * x * n)



n = 2
w = 4
cups = [1,1,1,1]

n = 3
w = 18
cups = [4,4,4,2,2,2]

n = 1
w = 5
cups = [2,3]

# n = 1 
# w = 1
# cups = [1000000000, 1000000000]

# first_line = list(map(int, input().split()))
# n = first_line[0]
# w = first_line[1]
# cups = list(map(int, input().split()))


solution = Answer()
result = solution.pashaAndTea(n, w, cups)
print(result)