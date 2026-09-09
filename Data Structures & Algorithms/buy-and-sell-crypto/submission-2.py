class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = 0 
        # right = 1
        # max_profit = 0 
        # while right < len(prices): 
        #     if prices[left] < prices[right]: 
        #         profit = prices[right]-prices[left]
        #         max_profit = max(max_profit,profit)
        #     else: 
        #         left = right
        #     right += 1 
        # return max_profit

        l = 0 
        r = 1 
        max_profit = 0 
        while r < len(prices):
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else: 
                l = r 
            r += 1 

        return max_profit

            