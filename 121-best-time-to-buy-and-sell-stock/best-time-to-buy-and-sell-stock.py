class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lower_price = 99999
        for i in range(len(prices)):
            lower_price = min(lower_price,prices[i])
            profit = max(profit , prices[i] - lower_price)
        return profit
        