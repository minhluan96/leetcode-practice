class Solution:
    def businessTrip(self, k, months):
        if k == 0:
            return 0

        months.sort(reverse=True)

        i = 0

        while i < len(months):
            k -= months[i]
            if k <= 0:
                break
            i += 1

        if k > 0:
            return -1
        
        return i + 1

# k = 5
# months = [1,1,1,1,2,2,3,2,2,1,1,1]

# k = 0
# months = [0,0,0,0,0,0,0,1,1,2,3,0]

# k = 11
# months = [1,1,4,1,1,5,1,1,4,1,1,1]

# k = 50
# months = [2,2,3,4,5,4,4,5,7,3,2,7]


k = int(input())
months = list(map(int, input().split()))

solution = Solution()
result = solution.businessTrip(k, months)
print(result)