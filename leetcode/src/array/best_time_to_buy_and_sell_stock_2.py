class Solution:
    def maxProfit(self, prices) -> int:
        min_price = -1
        arr = []

        for n in prices:
            if min_price == -1 or n < min_price or n - min_price > 0:
                if min_price != -1:
                    arr.append(n - min_price)
                
                min_price = n

        filtered = [i for i in arr if i > 0]
        return sum(filtered) if filtered else 0



class Solution2:
    '''
        Peak valley approach
    '''
    def maxProfit(self, prices) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                ''' will break if the prices[i] < prices[i+ 1] which mean it is the valley at i '''
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]

            max_profit += peak - valley
        
        return max_profit


class Solution3:
    ''' 
        Simple one pass
        follows the logic used in Approach 2 itself, but with only a slight variation. 
        In this case, instead of looking for every peak following a valley, 
            we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction. 
        In the end, we will be using the peaks and valleys effectively, 
            but we need not track the costs corresponding to the peaks and valleys along with the maximum profit,
            but we can directly keep on adding the difference between the consecutive numbers of the array if the second number is larger than the first one,
            and at the total sum we obtain will be the maximum profit
    '''

    def maxProfit(self, prices) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit

tc = [7,1,5,3,6,4]
solution = Solution3()
result = solution.maxProfit(tc)
print(result)