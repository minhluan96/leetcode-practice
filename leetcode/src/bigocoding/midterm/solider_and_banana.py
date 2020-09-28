class Solution:
    def solider_and_banana(self):
        total = w * (w + 1) // 2
        totalMoney = total * k
        if n >= totalMoney:
            return 0
        return totalMoney - n

if __name__ == '__main__':
    k, n, w = list(map(int, input().split()))
    solution = Solution()
    result = solution.solider_and_banana()
    print(result)