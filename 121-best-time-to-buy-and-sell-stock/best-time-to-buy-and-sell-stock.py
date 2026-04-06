class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lower_price = 99999
        for i in range(len(prices)):
            if prices[i]<lower_price:
                lower_price = prices[i]
            # lower_price = min(lower_price,prices[i])


            if prices[i] - lower_price > profit:
                profit = prices[i] - lower_price
            
        return profit
        