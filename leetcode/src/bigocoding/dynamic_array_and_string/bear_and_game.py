class Solution:
    def bear_and_game(self, n, times):
        default_minute = 15

        for t in times:
            if t <= default_minute:
                default_minute = t + 15
            else:
                break

        if default_minute > 90:
            default_minute = 90

        return default_minute


n = int(input())
times = list(map(int, input().split()))
solution = Solution()
result = solution.bear_and_game(n, times)
print(result)


