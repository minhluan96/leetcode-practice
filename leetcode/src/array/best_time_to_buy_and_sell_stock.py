class Solution:
    def maxProfit(self, prices):
        '''
            Complexity: O(n)
            Space complexity O(1)
        '''
        max_profit = 0
        min_price = -1
        if not len(prices): 
            return max_profit

        for n in prices:
            if min_price == -1 or n < min_price:
                min_price = n
            
            if max_profit < n - min_price:
                max_profit = n - min_price
                
        return max_profit

# [1, 2, 4]
tc = [2,4,1]
# [1, 3, 4, 5, 6, 7]
tc = [7,1,5,3,6,4]

tc = [2,1,2,0,1]
tc = [3,2,6,5,0,3]


solution = Solution()
result = solution.maxProfit(tc)
print(result)


