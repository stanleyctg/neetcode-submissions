class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        l, r = 0 ,1
        profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                curr_profit = prices[r] - prices[l]
                profit = max(profit, curr_profit)
                r += 1
        return profit
