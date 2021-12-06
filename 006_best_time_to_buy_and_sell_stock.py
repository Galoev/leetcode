class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            price = prices[i]

            best_profit = max(best_profit, price - min_price)
            min_price = min(min_price, price)

        return best_profit


# import numpy as np

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         best_profit = 0

#         for i, cur_price in enumerate(prices):
#             cur_prices = np.array(prices[i:])
#             profits = cur_prices - cur_price
#             cur_best_profit = np.max(profits)
#             if  cur_best_profit > best_profit:
#                 best_profit = cur_best_profit
                
#         return best_profit